from sty import fg,rs
import math
import time

class Calculator():
    def __init__(self):
        pass
    def add(self,no1,no2):
        return str(no1+no2)
    
    def subtract(self,no1,no2):
        return str(no1-no2)
    
    def multiply(self,no1,no2):
        return str(no1*no2)
    
    def divide(self,no1,no2):
        return str(no1/no2)

calc = Calculator()
print(fg.cyan + """

                _  _____      _       _             
          /\   | |/ ____|    | |     | |            
   ___   /  \  | | |    _   _| | __ _| |_ ___  _ __ 
  / __| / /\ \ | | |   | | | | |/ _` | __/ _ \| '__|
 | (__ / ____ \| | |___| |_| | | (_| | || (_) | |   
  \___/_/    \_\_|\_____\__,_|_|\__,_|\__\___/|_|   
                                                    
                                                    

""" + fg.rs)

time.sleep(1)
while True:
    print(fg.red + "Select operation to perform:\n")
    print(fg.li_blue + '[1] Addition')
    print('[2] Subtraction')
    print('[3] Multiplication')
    print('[4] Division')
    oper = int(input(fg.yellow + "\nEnter the number of your choice : " + fg.rs))

    no1 = int(input(fg.li_green + "\nEnter the first number: "))
    no2 = int(input(fg.da_green +"Enter the second number: "))

    if oper == 1:
        print(fg.magenta + "\nThe solution is " + fg.green + calc.add(no1,no2) + fg.rs)
    elif oper == 2:
        print(fg.magenta + "\nThe solution is " + fg.green + calc.subtract(no1,no2) + fg.rs)
    elif oper == 3:
        print(fg.magenta + "\nThe solution is " + fg.green + calc.multiply(no1,no2) + fg.rs)
    else:
        print(fg.magenta + "\nThe solution is " + fg.green + calc.divide(no1,no2) + fg.rs)
