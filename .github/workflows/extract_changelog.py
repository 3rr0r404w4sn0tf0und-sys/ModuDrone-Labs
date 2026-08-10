import os
import re
import json

def get_latest_changelog():
    changelog_path = "Changelog.md"
    if not os.path.exists(changelog_path):
        return {"title": "No Changelog Found", "description": "Changelog.md file is missing from repository root."}

    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return {"title": "Empty Changelog", "description": "Changelog.md file has no content."}

    # Find where markdown headings start
    heading_positions = [m.start() for m in re.finditer(r'^(#{1,6})\s', content, re.MULTILINE)]
    
    if not heading_positions:
        # If there are no markdown headers, treat the entire file as the message body
        return {"title": "Changelog Update", "description": content}

    # Isolate from the absolute first heading to the second heading (if it exists)
    start_pos = heading_positions[0]
    end_pos = heading_positions[1] if len(heading_positions) > 1 else len(content)
    latest_block = content[start_pos:end_pos].strip()

    lines = latest_block.split('\n')
    # Clean the first line to make it a clean title
    title = lines[0].replace('#', '').strip()
    
    # Reassemble everything else as the description body
    body_text = '\n'.join(lines[1:]).strip()

    # Scrub out all raw HTML image tags completely
    body_text = re.sub(r'<img[^>]*>', '', body_text)
    
    # Cap size limit for safety
    if len(body_text) > 4000:
        body_text = body_text[:3997] + "..."

    return {
        "title": title if title else "Changelog Update",
        "description": body_text if body_text else "New update committed."
    }

if __name__ == "__main__":
    data = get_latest_changelog()
    # Always guarantee clean, fallback JSON syntax outputs to environment channels
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
        fh.write(f"title={json.dumps(data['title'])}\n")
        fh.write(f"description={json.dumps(data['description'])}\n")
