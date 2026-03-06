def generate_diff(old, new):

    changes = []

    for key in new:

        if old.get(key) != new.get(key):

            changes.append({
                "field": key,
                "old": old.get(key),
                "new": new.get(key)
            })

    return changes


def write_changelog(path, changes):

    with open(path,"w") as f:

        for c in changes:

            f.write(f"{c['field']} changed\n")
            f.write(f"old: {c['old']}\n")
            f.write(f"new: {c['new']}\n\n")