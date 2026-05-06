def generate_TAC(expression):
    operators = set(['+', '-', '*', '/'])
    stack = []
    temp_count = 1

    print("Three Address Code:\n")

    for char in expression:
        if char == ' ':
            continue

        # If operand, push to stack
        if char not in operators:
            stack.append(char)
        else:
            # Pop two operands
            op2 = stack.pop()
            op1 = stack.pop()

            temp = f"t{temp_count}"
            temp_count += 1

            print(f"{temp} = {op1} {char} {op2}")

            # Push result back to stack
            stack.append(temp)

    print(f"\nFinal Result in: {stack[-1]}")


# Example usage
expr = "a+b*c"
# Convert to postfix manually for simplicity
# a+b*c → abc*+
postfix_expr = "abc*+"

generate_TAC(postfix_expr)
