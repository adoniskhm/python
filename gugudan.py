print(" * 구구단 * ")
for i in range(2, 10):
    print(f"\n<< {i}단 >>")
    for j in range(2, 10):
        result = i*j
        print (f"{i} X {j} = {result}")