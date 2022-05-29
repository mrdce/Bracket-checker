"""
Checks whether all brackets in the code are balanced.
Returns 'Success' if the brackets are balanced, returns numbered position of the first wrong bracket if not.
"""


def check_brackets(n):
    bracket_list = []
    counter = []
    index_c = -1
    for symbol in n:
        index_c += 1
        if symbol in ['(', '[', '{']:
            bracket_list.append(symbol)
            counter.append(index_c)
        elif symbol in [')', ']', '}']:
            if not bool(bracket_list):
                bracket_list.append(symbol)
                counter.append(index_c)
                break
            elif (bracket_list[-1] == '(' and symbol == ')') or (bracket_list[-1] == '[' and symbol == ']') or (
                    bracket_list[-1] == '{' and symbol == '}'):
                bracket_list.pop()
                counter.pop()
            else:
                bracket_list.append(symbol)
                counter.append(index_c)
                break
    if not bool(bracket_list):
        print('Success')
    elif bool(bracket_list):
        bad_index = counter[-1]
        print(bad_index + 1)


string = input()
check_brackets(string)
