def replace_instructions_v1(steps, replace):
    update_dir = []
    for each in steps:
        for e_replace in replace:
            if e_replace in each:
                each = each.replace(e_replace, replace[e_replace])
            elif e_replace in each.lower():
                each = each.lower().replace(e_replace, replace[e_replace])
        update_dir.append(each.strip())
    return update_dir


def replace_instructions(steps, replace):
    update_dir = []
    for step in steps:
        step_list = step.split(" ")
        for ing in replace:
            for i in range(1, len(step_list)):
                if (step_list[i - 1].lower() + " " + step_list[i].lower()) == ing:
                    step_list[i - 1] = replace[ing]
                    step_list[i] = ''
                elif step_list[i - 1].lower() == ing:
                    step_list[i - 1] = replace[ing]
                if i == len(step_list) - 1:
                    if step_list[i].lower() == ing:
                        step_list[i] = replace[ing]

        step_remade = " ".join(step_list)
        update_dir.append(step_remade)
    return update_dir
