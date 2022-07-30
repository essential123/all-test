# from typing import Optional


# class A(list):
#     def insert(self, location, value):
#         if value == 'mike':
#             print('mike不许插入')
#             return
#         super().insert(location, value)
#
#
# obj = A()
# obj.insert(0, 'tom')
# obj.insert(1, 'mike')
# obj.insert(2, 'jason')
# obj.insert(3, 'tony')
# print(obj)


class Student:
    school = '清华大学'

    def run(self):
        print('真服了你这个老六了')

    @classmethod
    def eat(cls):
        print('eat')

    @staticmethod
    def sleep():
        print('sleep')

stu = Student()
print(stu.run())
print(Student.run('self'))

print(Student.sleep())