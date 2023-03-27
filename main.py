from random import sample

bingo = [
    sample(range(0, 13), 5),
    sample(range(14, 26), 5),
    sample(range(27, 39), 5),
    sample(range(40, 52), 5),
    sample(range(53, 65), 5)
]

middle_of_the_bingo = "XXX"

bingo[2][2] = middle_of_the_bingo

for i in bingo:
    print(i)
