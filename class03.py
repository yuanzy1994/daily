# -*-coding:utf-8-*-
class JustCounter:
    __secretCount = 0
    publicCount = 0

    def __init__(self):
        pass

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

print counter.publicCount
# print counter.__secretCount  #私有方法 实例无法访问
print counter._JustCounter__secretCount
