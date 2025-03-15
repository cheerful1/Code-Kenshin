from abc import ABCMeta,abstractmethod

# 支付接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def payment(self, money):
        """支付抽象方法"""
        pass

# 具体支付实现
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def payment(self, money):  # 必须实现抽象方法（正确的方法名）
        if self.use_huabei:
            print(f"花呗支付{money}元")
        else:
            print(f"支付宝支付{money}元")

# 支付工厂接口
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        """创建支付对象"""
        pass

# 花呗支付工厂
class HuabeiFactory(PaymentFactory):
    def create_payment(self):  # 不需要money参数
        return Alipay(use_huabei=True)

if __name__ == "__main__":
    factory = HuabeiFactory()        # 创建工厂
    payment_method = factory.create_payment()  # 通过工厂创建支付对象
    payment_method.payment(100)      # 调用支付对象的payment方法