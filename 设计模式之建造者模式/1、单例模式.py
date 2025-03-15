#encoding=utf8
import threading
import time
#这里使用方法__new__来实现单例模式
class Singleton(object):#抽象单例
    def __new__(cls, *args, **kw):
        # 类中是否存在属性
        if not hasattr(cls, '_instance'):
            # 创建一个父类的实例
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


#总线
class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print ("Sending Signal Data...",data)
        self.lock.release()

#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)

if  __name__=="__main__":
    for i in range(3):
        print( "Entity %d begin to run..."%i)
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()