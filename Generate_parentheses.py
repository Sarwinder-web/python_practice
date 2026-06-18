def generate_parentheses(n, current, open_used, close_used):

    if len(current) == 2*n:
        print("".join(current))
        return

    if open_used < n:
        current.append("(")
        generate_parentheses(
            n,
            current,
            open_used +1,
            close_used
        )
        current.pop()
    
    if close_used < open_used:
        current.append(")")
        generate_parentheses(
            n,
            current,
            open_used,
            close_used +1
        )
        current.pop()

generate_parentheses(3, [], 0, 0)