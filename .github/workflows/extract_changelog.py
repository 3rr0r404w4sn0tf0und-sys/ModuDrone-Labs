import os
import re
import json
import urllib.request

def sync_to_discord():
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL environment variable is missing.")
        return

    changelog_path = "Changelog.md"
    if not os.path.exists(changelog_path):
        print("Changelog.md not found.")
        return

    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Only match level-2 headings (## ...) as "new entry" boundaries.
    # The old regex (`^#{1,3}\s`) also matched level-3 sub-headers like
    # "### Summary of Major Revisions", so heading_positions[1] pointed at
    # that sub-header instead of the *next entry*, truncating the body
    # right after the date line.
    #
    # NOTE: "---" horizontal rules are NOT used as entry boundaries here —
    # they're used repeatedly *within* a single entry to separate sections
    # (Summary / Milestones / Structural Improvements / BOM / Next Steps).
    # Only the next "## " heading marks the start of a new entry.
    heading_positions = [m.start() for m in re.finditer(r'^##\s', content, re.MULTILINE)]

    if not heading_positions:
        print("No headings found, sending full content.")
        title = "Changelog Update"
        body_text = content
    else:
        start_pos = heading_positions[0]
        end_pos = heading_positions[1] if len(heading_positions) > 1 else len(content)
        latest_block = content[start_pos:end_pos].strip()

        # Separate the title (the very first line) from the rest of the text
        lines = latest_block.split('\n')
        title = lines[0].replace('#', '').strip()
        body_text = '\n'.join(lines[1:]).strip()

    # Grid:{} blocks become <table>...</table> after format_changelog.py runs.
    # Discord embed descriptions can't render tables, so swap each one for a
    # short placeholder instead of dumping raw HTML into the message.
    body_text = re.sub(
        r'<table>.*?</table>',
        '🖼️ *[Image grid — view on GitHub]*',
        body_text,
        flags=re.DOTALL,
    )

    # Size:{} blocks become <details><summary>...</summary><img .../></details>.
    # Collapse each to a single placeholder line too.
    body_text = re.sub(
        r'<details>.*?</details>',
        '🖼️ *[Image — view on GitHub]*',
        body_text,
        flags=re.DOTALL,
    )

    # Clean out any remaining raw HTML image tags so they don't break the text block
    body_text = re.sub(r'<img[^>]*>', '', body_text)

    # Collapse any resulting blank-line runs left behind by stripped images
    body_text = re.sub(r'\n{3,}', '\n\n', body_text).strip()

    # Cap size limit safely within Discord's embed description boundary
    if len(body_text) > 4000:
        body_text = body_text[:3997] + "..."

    # Construct the complete JSON payload object structure
    payload = {
        "embeds": [{
            "title": title if title else "Changelog Update",
            "description": body_text if body_text else "New update committed.",
            "color": 3447003,
            "footer": {
                "text": "Automated CAD Sync"
            }
        }]
    }

    # Post the data to Discord over a native network stream
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'GitHub-Actions-Sync'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            print(f"Successfully posted to Discord! Response status: {response.status}")
    except Exception as e:
        print(f"Failed to deliver payload to Discord: {e}")

if __name__ == "__main__":
    sync_to_discord()
