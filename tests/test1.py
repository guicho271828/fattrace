
import traceback
from fattrace import err, format

def fn1():
    a = 1
    b = 0
    fn2(a,b)

def fn2(a,b):
    return a/b


class MultiLineString:
    def __repr__(self):
        return "aaa\nbbb\nccc"

class A():
    def __init__(self):
        self.x = 10
        self.y = B()
        self.field_name = 10
        # self.super_long_field_name = 10
        # self.gigantic_field_name = 10
        # self.long_gigantic_field_name = 10
        # self.stupidly_long_gigantic_field_name = 10
        # self.duper_stupidly_long_gigantic_field_name = 10
        self.super_duper_stupidly_long_gigantic_field_name = 10
        self.multi_line_string = MultiLineString()
    def m(self,y,
          super_duper_long_variable,
          *args):
        z = B()
        multi_line_string = MultiLineString()
        1/0

class B():
    def __str__(self):
        1/0
    def __repr__(self):
        1/0

try:
    fn1()
except Exception:
    err("## fancy stack trace ########################################")
    format(exit=False)
    err("## standard stack trace ########################################")
    traceback.print_exc()

try:
    a = A()
    a.m(3,4)
except Exception:
    err("## fancy stack trace ########################################")
    format(exit=False)
    err("## standard stack trace ########################################")
    traceback.print_exc()
