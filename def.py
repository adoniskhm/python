def sayParam(p1, p2, p3) :
    print(p1, p2, p3)
    print(p1, p2, p3)
    print(p1, p2, p3)
    return input("남기고 싶은 말을 입력하세요 : ")

result = sayParam("Hello!", "Good", "morning")

print(f"{result} 수고하셨습니다!")