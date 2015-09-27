from random import randint
import math


def isE(num1, num2):
    if num1<num2:
        print"too small"
        return False;
    if num1>num2:
        print"too big"
        return False;
    if num1==num2:
        print"ops"
        return True

    
x=2**100000
num=randint(1,x)
print"guess which number i like"
ops=False
while ops==False:
    answer=input()
    ops=isE(answer, num)
    
