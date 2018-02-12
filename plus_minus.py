# Given an array of integers, calculate which fraction of its elements are positive,
# which fraction of its elements are negative, and which fraction of its elements
# are zeroes, respectively. Print the decimal value of each fraction on a new line.


def plus_minus(a):
    pos_els = str(float(len([a.count(x) for x in a if x > 0])) / len(a))
    neg_els = str(float(len([a.count(x) for x in a if x < 0])) / len(a))
    zeroes = 0 or str(float(len([a.count(x) for x in a if x == 0])) / len(a))
    return '{}\n{}\n{}'.format(pos_els, neg_els, zeroes)


print plus_minus([1, 3, -6, 10, 30, -4])  # 4
