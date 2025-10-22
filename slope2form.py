print("""  

╔═╝╔═║╔═║╔╔ ══║╔═╝║  ╔═║╔═║╔═╝
╔═╝║ ║╔╔╝║║║╔═╝══║║  ║ ║╔═╝╔═╝
╝  ══╝╝ ╝╝╝╝══╝══╝══╝══╝╝  ══╝           Made 10/21/2025, by Isaac Tremblay
   """)

# Operation choice
print("What operation are you looking to do?")
print("1) Ax+By=C --> Y = Mx + B")
print("2) Y = Mx + B  --->  Ax+By=C")
print("3) Graph an equation")



#Conversion from standard data to slope



def operation1():
    print('\n')
    print("Great! Let's get started!")
    print("enter the values of; a, b, c. Inputting a string will return an error.")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    if b == 0:
        print(" your equation is a straight line (slope is undefined)")
    dequation = fr"{a:g}x+{b:g}y={c:g}"
    m = -a / b
    b = c / b
    slequation = fr"y = {m:g}x + {b:g}"
    print("Your equation in standard data format is: " + dequation)
    print("Your equation in slope intercept form is: " + slequation)



#Conversion from slope intercept to standard



def operation2():
    print("Great! Let's get started!")
    print("enter the values of; m & b")
    m = float(input("Enter the value of m: "))
    b = float(input("Enter the value of b: "))
    b_slope = b
    slequation = fr"y = {m:g}x + {b:g}"
    print("Your equation in slope intercept form is:" + slequation)
    a = -m
    b = 1
    c = b
    if a < 0:
        a, b, c = -a, -b, -c
    equation = fr"{a:g}x + {b:g}y = {c:g}"
    print("Your equation in standard data format is:" + equation)

#Slope intercept graphing


def operation3():
    import matplotlib.pyplot as plt
    import numpy as np
    m= float(input("enter the value of M: "))
    b= float(input("enter the value of B: "))
    equation = fr"y = {m:g}x + {b:g}"
    x = np.linspace(0, 50, 100)
    y = m*x + b
    xrange = float(input("Enter the range of x values: "))
    yrange = float(input("Enter the range of y values: "))
    plt.xlim(0, xrange)
    plt.ylim(0, yrange)
    plt.plot(x, y, label=fr"y = {m:g}x + {b:g}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Graph')
    plt.grid(True)
    plt.legend(["M", "B"])
    plt.show()
operation = input("Press the number corresponding to the operation: ")
if operation == "1":
    operation1()
if operation == "2":
    operation2()
if operation == "3":
    operation3()
