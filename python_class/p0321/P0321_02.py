class Student:

    def __init__(self,name = '',total = 0):
        self.name = name
        self.__total = total
    
    def __str__(self):
        return f'이름 : {self.name}, 합계 : {self.__total}'
    
    def set_total(self,total,login_id):
        if login_id == 'admin':
            self.__total = total
        else:
            print('admin 관리자가 아니면 수정이 불가능합니다.')

    def get_total(self):
        return self.__total
    
    # def __gt__(self,s):
    #     return self.total > s.total

    # def stu_print(self):
    #     print('학생성적 출력합니다.')

s = Student('홍길동',95)
s2 = Student('유관순',100)
# s.total = 300
s.set_total(400,'admin')
print(s.get_total())
# print(s)
# print(s)
# print(s2)
# # --- 
# print(s > s2)