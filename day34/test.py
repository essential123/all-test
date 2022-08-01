# class MyClass(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         # print('__str__方法')
#         return '对象:%s'%self.name
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#         print(args)
#         print(kwargs)
#     def __getattr__(self, item):
#         return '您想要获取的属性名: %s不存在'%item
#     def __setattr__(self, key, value):
#         print('__setattr__')
#         super().__setattr__(key, value)
#         pass
#     def __del__(self):
#         """对象在被删除(主动 被动)的时候自动触发"""
#         # print('__del__')
#         pass
#     def __getattribute__(self, item):
#         return super().__getattribute__(item)  # 简便写法
#     def __enter__(self):
#         print('__enter__')
#         return 123
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__')
# obj = MyClass('tom')
# with obj as f:
#     print(f)

# class Context:
#     pass
# with Context() as f:
#     f.do_something()
# class Context:
#     def __enter__(self):
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#     def do_something(self):
#         pass
# with Context() as f:
#     f.do_something()

# s1 = '哈哈哈'
# l2 = [60, 80, 100, 120, 150, 200]
# d = {'name': 'tom', 'age': 18}
# print(type(s1))  # <class 'str'>
# print(type(l2))  # <class 'list'>
# print(type(d))  # <class 'dict'>

# print(type(type))

# class MyClass1:
#     pass
# print(MyClass1.__dict__, MyClass1)
#
# res = type('MyClass2', (), {})
# print(res.__dict__, res)
# obj = res()
# print(obj)

# class MyMetaClass(type):
#     def __init__(self,what, bases=None, dict=None):
#         print('what', what)  # 类名
#         print('bases', bases) # 类的父类
#         print('dict', dict) # 类的名称空间
#         if not what.istitle():
#             print('首字母必须大写')
#         super().__init__(what, bases, dict)
# class aaa(metaclass=MyMetaClass):
#     pass
# class MyMetaClass(type):
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#         if args:
#             raise Exception('必须用关键字参数传参')
#         super().__call__(*args, **kwargs)
# class MyClass(metaclass=MyMetaClass):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('__init__')
# obj = MyClass('tom',18)


# class Student:
#     school = '清华大学'
#     def choice_course(self):
#         print('选课')
# attr = input('请输入属性名>>:').strip()
# value = input('请输入属性值>>:').strip()
# stu = Student()
# setattr(stu, attr, value)
# print(stu.__dict__)
# delattr(stu, attr)
# print(stu.__dict__)

# class Info:
#     d = {
#         'name': 'tom',
#         'age': 18,
#         'gender': 'male'
#     }


#
# k = input('请输入属性名>>:').strip()
# v = input('请输入属性值>>:').strip()
# obj = Info()
# print(obj.__dict__)
# if hasattr(obj.d, k):
#     setattr(obj.d, k, v)
#     print(f'修改了{k}键值对')
#
# else:
#     setattr(obj.d, k, v)
#     print(f'新增了一组键值对{k}:{v}')


# class Info(object):
#     def __init__(self,d):
#         for k,v in d.items():
#             d[k] = v
#     def __getattr__(self, k, v):
#         d[k] = v
#         print(f'修改键值对{k}:{v}')
#
#     def __setattr__(self, k, v):
#         d[k] = v
#         print(f'新增键值对{k}:{v}')
#
#
# d = {'name':'jzb', 'age':18}
# obj = Info(d)
# obj.name = 'tom'
# obj.hobby = 'game'
# print(obj.__dict__)

# d.key = value  修改键值对
# d.key = value  添加键值对


# class Info(object):
#     def __init__(self,key,value):
#         d[key] = value
#     def __getattr__(self,item,v):
#         self.k = v
#         print(f'修改键值对{item}:{v}')
#
#     def __setattr__(self, k, v):
#         super().__setattr__(k,v)
#         print(f'新增键值对{k}:{v}')
#
#
# d = {'name':'jzb', 'age':18}
# for key, value in d.items():
#     obj = Info(key,value)
# # d.name = 'tom'
# # d.hobby = 'game'
#     print(obj.__dict__)


# d.key = value  修改键值对
# d.key = value  添加键值对


# class Info(dict):
#     __setattr__ = dict.__setitem__
#     __getattr__ = dict.__getitem__
# d = Info()
# d.name = 'tom'
# print(d)
# d.name = 'jzb'
# d.hobby = 'game'
# print(d)

# d = {'name': 'jzb', 'age': 18}

# class ObjDict(dict):
#     def __getattr__(self, name):
#         try:
#             if d[name]:
#                 return d[name]
#         except:
#             raise AttributeError(name)
#     def __setattr__(self, name, value):
#         d[name] = value
# d = ObjDict()
# d.name ='tom'
# print(d)
# d.name = 'jzb'
# d.sex = 'male'
# print(d)

# class Student(object):
#     def __init__(self,name,age,gender):
#         self.name =name
#         self.age =age
#         self.gender = gender
#     def __setattr__(self, key, value):
#         pass
#     def __getattr__(self, item):
#         print('__getattr__')
#     def __getattribute__(self, item):
#         print('__getattribute__')
#
# stu = Student('tom',18,'male')

# print(stu.name)