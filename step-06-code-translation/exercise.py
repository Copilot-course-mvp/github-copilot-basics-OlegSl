def group_by_domain(emails: list[str]) -> dict[str, int]:
    """Translate the JavaScript behavior above into Python."""
    counts = {}
    for email in emails:
        if '@' not in email:
            continue
        domain = email.split('@')[1].strip().lower()
        if not domain:
            continue
        counts[domain] = counts.get(domain, 0) + 1
    return dict(sorted(counts.items()))