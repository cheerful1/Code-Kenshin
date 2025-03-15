# class Payment:
#     def pay(self,money):
#         # 继承的子类必须实现这个方法
#         raise NotImplemented
#
# #　第一种方法是继承的方法
# class AliPay(Payment):
#     def pay(self,money):
#         if money > 1000:
#             print("很多钱")
#
#
# class WechatPay:
#     def pay(self,money):
#         pass
#
# p = AliPay()
# p.pay(100000)


# # abc类是Python 标准库中用于定义抽象基类的工具
# from abc import ABCMeta, abstractmethod
#
# # ABCMeta 元类：在 Python 中，元类是用于创建类的“类”。ABCMeta 是一个特殊的元类，用于将当前类标记为抽象基类。
# class Payment(metaclass=ABCMeta):
#     @abstractmethod  #  装饰器。作用：标记一个方法为抽象方法，强制子类必须实现
#     def pay(self,money):
#         pass
# class AliPay(Payment):
#     # 必须自己实现这个抽象方法，如果自己没有实现这个方法，那自己本身也是一个抽象类
#     def pay(self,money):
#         if money > 1000:
#             print("很多钱")
#
# p = AliPay()
# p.pay(100000)


class User:
    def show_name(self,name):
        print(f"name{name}")

class VIPUser(User):
    def show_name(self,name):
        print(f"name:{name}")

user1 = VIPUser()
res = user1.show_name("zhangsan")