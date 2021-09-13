def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:
        first, operator, second = problem.split()

        if operator not in ('+', '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'

        if len(first) and len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        try:
            int(first)
            int(second)
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        max_length = max(len(first), len(second))
        result = eval(first + operator + second)

        first_line.append(first.rjust(max_length + 2))
        second_line.append(operator + ' ' + second.rjust(max_length))
        third_line.append((max_length + 2) * '-')
        fourth_line.append(str(result).rjust(max_length + 2))

    arranged_problems = '    '.join(first_line) + '\n'
    arranged_problems += '    '.join(second_line) + '\n'
    arranged_problems += '    '.join(third_line)

    if args:
        arranged_problems += '\n' + '    '.join(fourth_line)

    return arranged_problems
