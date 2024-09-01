def is_paired(input_string):

    pending_list = []
    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]

    output = True

    for c in input_string:
        if c in open_brackets:
            pending_list.append(c)

        elif c in closed_brackets:
            if len(pending_list) != 0:
                if c == ")" and pending_list[len(pending_list) - 1] == "(":
                    pending_list.pop()

                elif c == "]" and pending_list[len(pending_list) - 1] == "[":
                    pending_list.pop()

                elif c == "}" and pending_list[len(pending_list) - 1] == "{":
                    pending_list.pop()

                else:
                    output = False
            else:
                output = False

    if len(pending_list) > 0:
        output = False

    return output


print(is_paired("{[)][]}"))
