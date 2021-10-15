#finds square root of an int
import sys
string = input("Enter an integer to find the square root: ")
precision = input("To how many decimal places would you like the square root? ")
length = len(string)
num = int(string)
org = num
one = 1;
while((one*one) < num):
    one=one+1
if((one*one)==num):
    print("The square root of " + str(num) + " is " + str(one))
    sys.exit()
elif(one*one > num):
    one=one-1
    newnum = one
    for i in range(0, int(precision)):
        num=num*100
        one=one*10
        while((one*one) < num):
            one=one+1

        if((one*one) > num):
            one=one-1


#print(str(one))
rm = str(one)
newum = str(newnum)
x = rm.replace(newum, "", 1)
print("The square root of " + str(org) + " is " + (str(newum)+"."+x))
sys.exit()
