#-*-coding:utf-8-*-


class MyException(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

a = 4
if a < 10:

    try:
        raise MyException("raise exception!")
    except MyException, e:
        print "触发异常:", e.message
    else:
        print "没有触发异常!"
