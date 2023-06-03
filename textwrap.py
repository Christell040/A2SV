import textwrap

def wrap(string, max_width):
    wrapped_string = textwrap.wrap(string, max_width)
    return wrapped_string

string = input()
max_width = int(input())

result = wrap(string, max_width)
for line in result:
    print(line)