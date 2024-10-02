import random

pBalls = 6
history = {}
for i in range(1, 46):
    history[i] = 0

def lotto(li):
    drawn_numbers = []
    for z in range(pBalls):
        num = random.randint(0, len(li) - 1)
        drawn_numbers.append(li[num])
        history[li[num]] += 1
        del li[num]
    return drawn_numbers

for i in range(100):
    numbers = list(range(1, 46))
    result = lotto(numbers)
    print(f" {i + 1}: {sorted(result)}")

print(history)
