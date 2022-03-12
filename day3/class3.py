class Vehicle:
    name = " "
    kind = 'car'
    color = " "
    value = 100.00
    def discription(self):
        des = ("%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value))
        return des

car1 = Vehicle()
car1.name = 'Fer'
car1.color = 'red'
car1.kind =  'convertiable'
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.discription())
print(car2.discription())