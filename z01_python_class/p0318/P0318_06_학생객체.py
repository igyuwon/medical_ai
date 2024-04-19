class Student: #클래스선언 - 설계도
    # stuNo = 0
    # stu_name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0

    def __init__(self, stuNo=0, stu_name='', kor=0, eng=0, math=0):
        self.stuNo = stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total / 3))
        self.rank = 0

# 1,홍길동,99,99,87,285,95.0,1
# 2,유관순,98,93,87,278,92.67,3
# 3,이순신,88,76,30,194,64.67,6
        
stu1 = Student() #객체선언 - 제품생산
stu1.stuNo = 1
stu1.stu_name = '이순신'
stu1.kor = 99
stu1.eng = 99
stu1.math = 87
stu1.total = stu1.kor + stu1.eng + stu1.math
stu1.avg = float("{:.2f}".format(stu1.total / 3))
stu1.rank = 1
print('번호\t이름\t국어\t영어\t수학\t총합\t평균\t등수')
print(f"{stu1.stuNo}\t{stu1.stu_name}\t{stu1.kor}\t{stu1.eng}\t{stu1.math}\t{stu1.total}\t{stu1.avg}\t{stu1.rank}")

stu2 = Student(2,'유관순',98,93,87)
print(f"{stu2.stuNo}\t{stu2.stu_name}\t{stu2.kor}\t{stu2.eng}\t{stu2.math}\t{stu2.total}\t{stu2.avg}\t{stu2.rank}")

stu3 = Student(3,'이순신',88,76,30)
print(f"{stu3.stuNo}\t{stu3.stu_name}\t{stu3.kor}\t{stu3.eng}\t{stu3.math}\t{stu3.total}\t{stu3.avg}\t{stu3.rank}")

# 3명의 학생을 리스트에 추가
stu_list = [stu1,stu2,stu3]