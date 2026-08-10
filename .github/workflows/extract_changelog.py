import os
import re
import json

def get_latest_changelog():
    changelog_path = "Changelog.md"
    if not os.path.exists(changelog_path):
        return None

    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return None

    # Find where markdown headings start
    heading_positions = [m.start() for m in re.finditer(r'^(#{1,6})\s', content, re.MULTILINE)]
    
    if not heading_positions:
        title = "Changelog Update"
        body_text = content
    else:
        # Isolate from the absolute first heading to the second heading
        start_pos = heading_positions[0]
        end_pos = heading_positions[1] if len(heading_positions) > 1 else len(content)
        latest_block = content[start_pos:end_pos].strip()

        lines = latest_block.split('\n')
        title = lines[0].replace('#', '').strip()
        body_text = '\n'.join(lines[1:]).strip()

    # Scrub out all raw HTML image tags completely
    body_text = re.sub(r'<img[^>]*>', '', body_text)
    
    # Cap size limit for safety
    if len(body_text) > 4000:
        body_text = body_text[:3997] + "..."

    # Create the exact JSON layout object structure here in Python
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
    
    return payload

if __name__ == "__main__":
    data = get_latest_changelog()
    if data:
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
            # We dump the raw string directly without extra shell escaping loops
            fh.write(f"payload={json.dumps(data, ensure_ascii=False)}\n")
