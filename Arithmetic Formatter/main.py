def arithmetic_arranger(problems, show_answers=False):
    # If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if not (num1.isdigit() and num2.isdigit()):
            # Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
            return "Error: Operator must be '+' or '-'."
        # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(width) + "    "
        second_line += operator + num2.rjust(width - 1) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            result_line += result.rjust(width) + "    "

    arranged_problems += first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()
    if show_answers:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
