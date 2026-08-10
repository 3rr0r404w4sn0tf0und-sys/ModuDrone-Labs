import os
import re
import json

def get_latest_changelog():
    changelog_path = "Changelog.md"
    if not os.path.exists(changelog_path):
        return None

    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split the document precisely when the Engineering update header format is encountered
    sections = re.split(r'^(?=##\s+🛠️\s+Engineering Update)', content, flags=re.MULTILINE)
    
    if len(sections) < 2:
        if not sections:
            return None
        latest_block = sections
    else:
        # If text exists before the first header, skip it and pick the first true update section
        latest_block = sections if sections.strip() == "" else sections

    latest_block = latest_block.strip()

    # Isolate lines to separate the heading title from the technical logs
    lines = latest_block.split('\n')
    title = lines.replace('##', '').strip()
    
    body_text = '\n'.join(lines[1:]).strip()

    # Strip out the raw HTML img tags that clutter and break text formatting arrays
    body_text = re.sub(r'<img\s+[^>]*\/>', '', body_text)
    
    # Cap string outputs safe from Discord structural container failures
    if len(body_text) > 4000:
        body_text = body_text[:3997] + "..."

    return {
        "title": title,
        "description": body_text
    }

if __name__ == "__main__":
    data = get_latest_changelog()
    if data:
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as fh:
            fh.write(f"title={json.dumps(data['title'])}\n")
            fh.write(f"description={json.dumps(data['description'])}\n")
