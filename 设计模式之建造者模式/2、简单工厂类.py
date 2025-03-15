# abc类是Python 标准库中用于定义抽象基类的工具
from abc import ABCMeta, abstractmethod

# ABCMeta 元类：在 Python 中，元类是用于创建类的“类”。ABCMeta 是一个特殊的元类，用于将当前类标记为抽象基类。
class Payment(metaclass=ABCMeta):
    @abstractmethod  #  装饰器。作用：标记一个方法为抽象方法，强制子类必须实现
    def pay(self,money):
        pass
class AliPay(Payment):
    # 必须自己实现这个抽象方法，如果自己没有实现这个方法，那自己本身也是一个抽象类
    def pay(self,money):
        if money > 1000:
            print("很多钱")


class WechatPay(Payment):
    # 必须自己实现这个抽象方法，如果自己没有实现这个方法，那自己本身也是一个抽象类
    def pay(self,money):
        if money > 1000:
            print("很多钱111")


class PaymentFactory:
    def create_payment(self,method):
        if method == "AliPay":
            return AliPay()
        elif method == "WechatPay":
            return WechatPay()
        else:
            raise TypeError("no")

nf = PaymentFactory()
p = nf.create_payment("AliPay")
p.pay(10010)

# 隐藏内部实现