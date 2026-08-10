import os
import re
import json
import urllib.request

def sync_to_discord():
    # 1. Fetch the secure webhook URL from the repository settings environment
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL environment variable is missing.")
        return

    changelog_path = "Changelog.md"
    if not os.path.exists(changelog_path):
        print("Changelog.md not found.")
        return

    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        print("Changelog.md is empty.")
        return

    # 2. Extract from the absolute first heading to the second heading
    heading_positions = [m.start() for m in re.finditer(r'^(#{1,6})\s', content, re.MULTILINE)]
    
    if not heading_positions:
        title = "Changelog Update"
        body_text = content
    else:
        start_pos = heading_positions[0]
        end_pos = heading_positions[1] if len(heading_positions) > 1 else len(content)
        latest_block = content[start_pos:end_pos].strip()

        lines = latest_block.split('\n')
        title = lines[0].replace('#', '').strip()
        body_text = '\n'.join(lines[1:]).strip()

    # 3. Clean out all HTML image tags cleanly
    body_text = re.sub(r'<img[^>]*>', '', body_text)
    
    # Cap size limit safely within Discord's 4096 embed description boundary
    if len(body_text) > 4000:
        body_text = body_text[:3997] + "..."

    # 4. Construct the complete final JSON object payload structure
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

    # 5. Safely POST the payload out to Discord over a native network stream
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
