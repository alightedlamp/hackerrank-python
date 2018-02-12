def solve(a0, a1, a2, b0, b1, b2):
    array = list(zip((a0, a1, a2), (b0, b1, b2)))
    score = 0, 0
    for t in array:
        if t[0] > t[1]:
            score = (score[0] + 1, score[1])
        elif t[0] < t[1]:
            score = (score[0], score[1] + 1)
    return ' '.join([str(s) for s in score])


print solve(5, 6, 7, 3, 6, 10)
