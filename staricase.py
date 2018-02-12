# Print a staircase of size N using # symbols and spaces.
def staircase(n):
    staircase = ''
    for i in range(n):
        staircase += " " * (n - 1 - i)
        staircase += "#" * (i + 1)
        staircase += "\n"
    return staircase


print staircase(6)
