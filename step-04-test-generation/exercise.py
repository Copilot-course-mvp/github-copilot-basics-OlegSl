import re


def sanitize_tags(tags: list[str]) -> list[str]:
    """Normalize user tags.

    Rules:
    - Lowercase
    - Trim whitespace
    - Remove non alphanumeric chars (except '-')
    - Remove empty tags after cleanup
    - Deduplicate while preserving first-seen order
    """
    cleaned: list[str] = []
    for tag in tags:
        normalized = tag.strip().lower()
        normalized = re.sub(r"[^a-z0-9-]", "", normalized)
        if not normalized:
            continue
        if normalized in cleaned:
            continue
        cleaned.append(normalized)
    return cleaned