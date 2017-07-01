# -*-coding:utf-8-*-
class Parent:
    parentAttr = 100

    def __init__(self):
        print "父类构造函数"

    def parentMethod(self):
        print "父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr
        a = getattr(Parent, 'parentAttr')
        print "设置父类属性: %d" % a

    def getAttr(self):
        b = getattr(Parent, 'parentAttr')
        print "获取父类属性：%d" % b


class Child(Parent):

    def __init__(self):
        print "子类构造函数"

    def childMethod(self):

        print "子类方法"

s = Child()

s.childMethod()
s.parentMethod()
s.getAttr()
s.setAttr(666)
