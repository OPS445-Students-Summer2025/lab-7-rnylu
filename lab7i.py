#!/usr/bin/env python3
# Student ID: rlu22
def function1():
    global schoolName # made function1's schoolName variable global
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:',schoolName)
function1()
print('print() in main on schoolName:',schoolName)
function2()
print('print() in main on schoolName:',schoolName)