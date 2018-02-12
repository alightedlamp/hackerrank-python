def mini_max_sum(n):
    # remove .split()'s to accept array as input per HR test cases
    sums = [sum([int(j) for j in n.split()]) - int(i) for i in n.split()]

    print sorted(sums)[0], sorted(sums)[-1]


mini_max_sum("5 5 5 5 5")
