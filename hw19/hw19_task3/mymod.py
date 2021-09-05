

def count_lines(filepath):
    with open(filepath, 'r+') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(filepath):
    with open(filepath, 'r+') as file:
        chars = file.read()
        return len(chars)

def test(filepath):
    num_of_lines = count_lines(filepath)
    print(num_of_lines)
    num_of_chars = count_chars(filepath)
    print(num_of_chars)

test('text_file.txt')