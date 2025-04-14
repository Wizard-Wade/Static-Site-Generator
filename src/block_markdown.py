def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        block = block.strip()
        if block:
            filtered.append(block)
    return filtered
