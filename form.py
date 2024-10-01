formcode = "제 몸무게는 %dkg 입니다."

boy1 = formcode % 70
boy2 = formcode % 55

print(boy1)
print(boy2)

'''
%s 문자열
%d 정수
%f 부동 소수
%c 단일 문자
%% 퍼센티지 기호
'''

form = "%20.4f"

print(form % 3.14)

form = "%1.0f"
print(form % 3.14)

age = 100
wording = f"내 나이는 {age}살 입니다."
print(wording)