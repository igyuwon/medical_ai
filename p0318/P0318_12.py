# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo에는 CarCount 숫자를 이용해서 carNo를 넣으시오.
# carNo, color = "white", door=5, tire=4
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 -10씩 감소

# c1 - 1,white,5,4,0 -> speed 30이 되도록
# c2 - 2,red,5,4,0 -> speed 100
# c3 - 3,silver,5,4,0 -> speed 79
# car_list 추가하고

# car_list 에 있는 모든 객체의 모든 color,door,tire,speed 모두 출력하세요.
class Car():
    carCount = 0
    carNo = 0

    def __init__(self,color = "",door="",tire="",speed = ""):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1
        self.carNo = Car.carCount
    def up_speed(self):
        self.speed += 10

    def down_speed(self):
        self.speed -= 10

    # def car_print(self):
    #     print(self.carNo, self.color, self.door, self.tire, self.speed)

car_list = []

c1 = Car("white",5,4,0)
for i in range(3):
    c1.up_speed()
print(c1.carNo, c1.color, c1.door, c1.tire, c1.speed)
car_list.append([c1.carNo, c1.color, c1.door, c1.tire, c1.speed])

c2 = Car("red",5,4,0)
for i in range(10):
    c2.up_speed()
print(c2.carNo, c2.color, c2.door, c2.tire, c2.speed)
car_list.append([c2.carNo, c2.color, c2.door, c2.tire, c2.speed])
c3 = Car("silver",5,4,0)
for i in range(7):
    c3.up_speed()
print(c3.carNo, c3.color, c3.door, c3.tire, c3.speed)
car_list.append([c3.carNo, c3.color, c3.door, c3.tire, c3.speed])
# c1.car_print()
# c2.car_print()
# c3.car_print()

print(car_list)
    