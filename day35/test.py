# class MyMetaClass(type):
#     instance = None
#     def __call__(self, *args, **kwargs):
#         if self.instance:
#             return self.instance
#         obj = super().__call__(*args, **kwargs)
#         self.instance =obj
#         return obj
# class Single(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name =name
# obj1 = Single('tom')
# obj2 = Single('kevin')
# obj3 = Single('tony')
# print(obj1.name,id(obj1))
# print(obj2.name,id(obj2))
# print(obj3.name,id(obj3))

# import pickle
# with open(r'a.txt','wb')as f:
#     f.write(pickle.dump(f))
#


# class Student():
#     def __init__(self, name):
#         self.name = name
# stu = Student('jason')
# print(stu.__class__, type(stu.__class__))
# print(stu.__class__.__name__, type(stu.__class__.__name__))
# print(Student.__name__, type(Student.__name__))

