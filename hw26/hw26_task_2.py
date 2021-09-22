# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."
from Stack import Stack

def AreBracketsBalanced(expr):
    if not expr:
        return 'Empty'

    stack = Stack()
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "[", "<"]:
            # Push the element in the stack
            stack.push(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    stack.push(current_char)
                    break
            if current_char == '{':
                if char != "}":
                    stack.push(current_char)
                    break
            if current_char == '[':
                if char != "]":
                    stack.push(current_char)
                    break
            if current_char == '<':
                if char != ">":
                    stack.push(current_char)
                    break
    # Check Empty Stack
    if stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"

if __name__ == "__main__":
    string1 = "{[]{()}}"
    print(string1, "-", AreBracketsBalanced(string1))

    string2 = "[{}{})(]"
    print(string2, "-", AreBracketsBalanced(string2))

    string3 = "((()"
    print(string3, "-", AreBracketsBalanced(string3))