def replace_instructions(steps, replace):
    update_dir = []
    for each in steps:
        for e_replace in replace:
            if e_replace in each:
                each = each.replace(e_replace, replace[e_replace])
                break
            elif e_replace in each.lower():
                each = each.lower().replace(e_replace, replace[e_replace])
                break
        update_dir.append(each.strip())
    return update_dir
