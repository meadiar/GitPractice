example = 5
print('int'+str(example))
#
condition = 1
while condition < 10:
    print(condition)
    condition += 1
x, y = 3, 5
print(x)
print(y)

exList = [3,4,5,6,54]

for i in range(5):
    print(i)

def show():
    print('it is the result')

show()

def addnum(num1,num2=2):
    answer = num1 + num2
    print('num1 + num2 = ', answer)

addnum(4)

#global xi
xi = 6

def glo():
##    global xi
    print(xi)
    h = xi
    h += 5
    print(h)

glo()
print(xi)

#
