# -*- coding: utf-8 -*-
number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False # this causes the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else: #这个else可省略，然后把print放到while外边~
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'

#——————————————————————————————————————————————————————————————————————————
print "______________________________________6.3________________________________________"

"""
for循环

|range()函数形成一个序列，参数（start,stop,step）
"""
for i in range(1, 5):
    print i
else:
    print 'The for loop is over'


#——————————————————————————————————————————————————————————————————————————
print "______________________________________6.4________________________________________"


while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
print 'Done'

#——————————————————————————————————————————————————————————————————————————
print "______________________________________6.5________________________________________"


while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length'
