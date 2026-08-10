import re

# Standard display width (px) applied to every image, whether it's inside
# a Size:{} block or a Grid:{} block. Change this in one place to restyle
# every image in the changelog at once.
STANDARD_WIDTH = 600

IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
SRC_RE = re.compile(r'src\s*=\s*"([^"]+)"', re.IGNORECASE)
ALT_RE = re.compile(r'alt\s*=\s*"([^"]*)"', re.IGNORECASE)


def _extract_src_alt(img_tag: str):
    src_match = SRC_RE.search(img_tag)
    alt_match = ALT_RE.search(img_tag)
    src = src_match.group(1) if src_match else ""
    alt = alt_match.group(1) if alt_match else "image"
    return src, alt


def _build_img(src: str, alt: str, width: int) -> str:
    return f'<img src="{src}" alt="{alt}" width="{width}" />'


def _replace_size_block(match: re.Match) -> str:
    inner = match.group(1)
    img_tags = IMG_TAG_RE.findall(inner)
    if not img_tags:
        return match.group(0)  # leave untouched if nothing found

    # Size:{} supports multiple images too, but stacks them individually
    # (each gets its own bordered/expandable box) rather than gridding
    # them side by side — that's what Grid:{} is for.
    blocks = []
    for tag in img_tags:
        src, alt = _extract_src_alt(tag)
        img_html = _build_img(src, alt, STANDARD_WIDTH)
        blocks.append(
            "<details>\n"
            f"<summary>📷 {alt}</summary>\n\n"
            f"{img_html}\n"
            "</details>"
        )

    return "\n\n".join(blocks)


def _replace_grid_block(match: re.Match) -> str:
    inner = match.group(1)
    img_tags = IMG_TAG_RE.findall(inner)
    if not img_tags:
        return match.group(0)

    cells = []
    for tag in img_tags:
        src, alt = _extract_src_alt(tag)
        img_html = _build_img(src, alt, STANDARD_WIDTH)
        cells.append(f"<td>{img_html}</td>")

    row = "<tr>\n" + "\n".join(cells) + "\n</tr>"
    return f"<table>\n{row}\n</table>"


def format_changelog(content: str) -> str:
    # Size:{ ... } -> single standardized, expandable image
    content = re.sub(
        r"Size:\{\s*(.*?)\s*\}",
        _replace_size_block,
        content,
        flags=re.DOTALL,
    )

    # Grid:{ ... } -> HTML table row of standardized images
    content = re.sub(
        r"Grid:\{\s*(.*?)\s*\}",
        _replace_grid_block,
        content,
        flags=re.DOTALL,
    )

    return content


def main():
    path = "Changelog.md"
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    updated = format_changelog(original)

    if updated == original:
        print("No Grid:{} or Size:{} blocks found — nothing to do.")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)

    print("Changelog.md updated: Grid:{} and Size:{} blocks converted to HTML.")


if __name__ == "__main__":
    main()
