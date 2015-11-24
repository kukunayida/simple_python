# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print 'The command line arguments are:'

for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

print dir(sys)

a =5
print dir()


del a

print dir()

k =["d","e","q","a","e2","b"]
print k.sort()
print kr

la = """知乎新手 要答题了有一点点小激动哈哈哈哈 ---学生党 不过在德克士里面上班做兼职已经快三年了 表"""
print sys.getdefaultencoding()
print la
print type(la)
la =  la.split(" ")
print len(la)
print la[0]

la = "知乎新手"
print len(la)
"""unicode中汉字为两字节, utf-8中汉字为三字节"""