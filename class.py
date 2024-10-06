# class Cat:
#     def meow(self):
#         print("야옹~~")

# Cat()

class Korean :
    nation = "대한민국"
    def sayHello(self) :
        print("안녕하세요!")

class Chinese :
    def sayHello(self, name) :
        print("你好" + name)

k = Korean()
c = Chinese()

k.sayHello()
c.sayHello("我是权赫民")

print(k.nation)