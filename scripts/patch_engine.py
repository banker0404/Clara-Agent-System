def apply_patch(old_memo, updates):

    new_memo = old_memo.copy()

    for key, value in updates.items():

        if isinstance(value, dict) and key in new_memo:
            new_memo[key].update(value)
        else:
            new_memo[key] = value

    return new_memo