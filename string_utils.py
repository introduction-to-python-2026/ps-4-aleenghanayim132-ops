def split_before_each_uppercases(formula):
    start = 0
    end = len(formula) + 1
    split_formula = []
    for i in range(start + 1, end):
      if i == end - 1 or formula[i].isupper():
        split_formula.append(formula[start:i])
        start = i
    return split_formula

def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
      if ch.isdigit():
        break
      digit_location += 1
    if digit_location == len(formula):
      return (formula, 1)
    if digit_location < len(formula):
      return (formula[:digit_location], int(formula[digit_location:]))
