import random

# for i in range(10) :
#     print(random.randint(1, 10))

# i = 0
# while i < 10 :
#     print(random.randint(1, 10))
#     i += 1

lotto = []

while len(lotto) < 6 :
    rn = random.randrange(1, 46)
    if rn in lotto :
        pass
    else :
        lotto.append(rn)

lotto.sort()
print(lotto)