# -*- coding: utf-8 -*-
#——————————————————————————————————————————————————————————————————————————
print "______________________________________7.3局部变量________________________________________"

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50

func(x)
print 'x is still', x


#——————————————————————————————————————————————————————————————————————————
print "______________________________________7.4 global________________________________________"


def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'Value of x is', x