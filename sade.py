class Computer:
    def calculate(self):
        print("Calculating...")
class Display:
    def display(self):
        print("I display the image on the screen... ")
class SmartPhone(Display,Computer):
    pass
iphone=SmartPhone()
iphone.calculate()
iphone.display()



