#!usr/bin/env python
#-*-coding: utf-8 -*-

print """Witaj
w swiecie Pythona"""
print "Witaj w swiecie Pythona"
print '"Witaj w świecie Pythona"'
a = "Witaj w \n"
b = 'Świecie Pythona '
c = 14
print a[0]
print a[0:5]
print a+b+str(c)
print b+repr(c)

x = 16.0
y = 3
if x < y :
    a = 'y:x'
    score = y/x
elif x == y :
    a = 'x = y'
    score = 1
elif x > y and y < c :
    a = 'c modulo x'
    score = c%x
else:
    a = 'x:y'
    score = x/y

print "%s=%.2f" % (a,score)

colors = ["red", 'green', 'yellow']
print colors
print colors[1]
print len(colors)
print len(colors[2])
colors.append("white")
print colors
print list(colors)
tupla = (1,3,'third')
print tupla
s = "&"
print s.join(colors)
colors[0].capitalize()
print colors

colors.reverse()
print colors
colors.append(29)
print colors
colors.extend(tupla)
print colors

for i in b:
    print i

numbers = ['one','two','three','four','five']

for i in numbers:
    print i

for i in range(1,5,2):
    print numbers[i]

counter = 0
while counter <= 5:
    if counter < len(numbers):
        print "%s %s" % ("I am in for",numbers[counter])
    else:
        print '\t Index ' + str(counter) + " doesn't exist"
    counter += 1

data_assoc = {'name':'Artur','surname':'Wilczak','age':36,'sex':'male','height':179,'weight':''}

for i in data_assoc:
    print "%s: %s" % (i,data_assoc[i])

print '\n'

if data_assoc.has_key('sex'):
    print 'sex: ' + data_assoc['sex']
else:
    print 'N/A'

print data_assoc.get('height','N/A')
print data_assoc.get('weight','N/A')

print list(data_assoc.keys())
del data_assoc['sex']
print list(data_assoc.keys())

''' comment
multi lines
'''
# comment one line

# next chapter: Function