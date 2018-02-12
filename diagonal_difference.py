# Given a square matrix of size N x N, calculate the absolute difference between the sums of its diagonals.
def diag_diff(arr):
    # This line enables a string as input
    # arr = [x.split() for x in arr.split('\n')]
    primary_diag_sum = 0
    secondary_diag_sum = 0
    for i, j in enumerate(arr):
        primary_diag_sum += int(j[i])
    for i, j in enumerate(arr[::-1]):
        secondary_diag_sum += int(j[i])

    return abs(primary_diag_sum - secondary_diag_sum)


print diag_diff('11 2 4\n4 5 6\n10 8 -12')
