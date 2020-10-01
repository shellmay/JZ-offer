
def cutRope( number):
    # write code here
    if number<=4:
        return number
    number1=number//3
    if number-number1*3==1:
        number1-=1
    number2=(number-number1*3)//2
    print(number1,number2)
    return pow(3,number1)*pow(2,number2)

print(cutRope(3))