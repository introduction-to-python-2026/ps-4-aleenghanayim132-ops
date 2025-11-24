def split_before_each_uppercases(formula):
    start = 0
    list_of_parts = []
    for i in range(len(formula)):
        if formula[i].isupper():
            list_of_parts.append(formula[start:i])
            start = i
    list_of_parts.append(formula[start:])
    return list_of_parts


def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1

