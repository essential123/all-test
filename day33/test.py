# class Student(object):
#     __school = '清华大学'
#     def __init__(self,name):
#         self.__name = name
#     def set_info(self):
#         return self.__name
#
# stu1 = Student('jason')
#
# print(stu1.set_info())
# # print(_Student.__name)


# class Person:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def BMI(self):
#         return self.weight / (self.height ** 2)
#
#
# p1 = Person('悍匪', 72, 1.73)
# print(p1.BMI)


# class Foo:
#     def __init__(self, val):
#         self.__NAME = val  # 将属性隐藏起来
#
#     @property
#     def name(self):
#         return self.__NAME
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):  # 在设定值之前进行类型检查
#             raise TypeError('%s must be str' % value)
#         self.__NAME = value  # 通过类型检查后,将值value存放到真实的位置self.__NAME
#
#     @name.deleter
#     def name(self):
#         raise PermissionError('Can not delete')
#
#
# obj = Foo('jason')
# print(obj.name)
# obj.name = 'tom'
# print(obj.name)
# del obj.name


# import abc
# # 指定metaclass属性将类设置为抽象类，抽象类本身只是用来约束子类的，不能被实例化
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod # 该装饰器限制子类必须定义有一个名为talk的方法
#     def talk(self): # 抽象方法中无需实现具体的功能
#         pass
# class Person(Animal): # 但凡继承Animal的子类都必须遵循Animal规定的标准
#     def talk1(self):
#         pass
#     def run(self):
#         pass
# obj = Person()


# class Student:
#     school = '清华大学'
#     def choice_course(self):
#         print('选课')
# stu = Student()
# print(stu.__dict__)
# stu.name = 'jason'
# stu.age = 18
# print(stu.__dict__)
# setattr(stu,'gender','male')
# setattr(stu,'hobby','read')
# print(stu.__dict__)
# del stu.name
# print(stu.__dict__)
# delattr(stu, 'age')
# print(stu.__dict__)

class A():
    name = 'runoob'
a =A()
setattr(a,'age',28)
print(a.age,type(a.age))