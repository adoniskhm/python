# i = 6

# if i <= 5 :
#     print(f"{i}는 5보다 작거나 같습니다.")
# else:
#     print(f"{i}는 5보다 큽니다.")

password = 1827

pass_input = int(input("패쓰워드를 입력하세요 : "))

if pass_input == password:
    print("로그인 되었습니다. 환영합니다!")
else:
    print("비밀번호가 틀립니다.")