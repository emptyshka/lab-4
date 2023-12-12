def sol(n):
    VALUES = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
    WEIGHTS = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]
    ITEMS = ['r', 'p', 'a', 'm', 'i', 'k', 'x', 't', 'f', 'd', 's', 'c']
    cap = n
    score = 15
    prod = []
    liters = []

    for i in range(len(VALUES)):
        prod.append((VALUES[i] / WEIGHTS[i], i))
    prod.sort()

    for i in reversed(range(len(prod))):
        weight = WEIGHTS[prod[i][1]]
        if cap - weight >= 0:
            cap -= weight
            score += weight * prod[i][0]
            for _ in range(weight):
                liters.append([ITEMS[prod[i][1]]])
        else:
            score -= weight * prod[i][0]
    return liters, score


TASK_NUM = 8
ans, score = sol(TASK_NUM)
for i in range(0, TASK_NUM - 1, 2):
    print(ans[i], ans[i + 1])
print(f'Total value - {int(score)}')