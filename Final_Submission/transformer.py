def replace_instructions(steps, replace):
    update_dir = []
    for each in steps:
        for e_replace in replace:
            if e_replace in each:
                each = each.replace(e_replace, replace[e_replace])
        update_dir.append(each)                    
    return update_dir