import random
total_try = 500000
inner_try = 0
test = [0.699, 0.703, 0.707, 0.711, 0.715]
for i in test:
    inner_try = 0
    for _ in range(total_try):
        x = random.random()
        y = random.random()
        r = (x**2+y**2)**0.5
        while r > 1:
            x = random.random()
            y = random.random()
            r = (x**2+y**2)**0.5
        if r < i:
            inner_try += 1
    print(i, " : ", inner_try/total_try)
