class Person:
    def __init__(self,name,age,pay=0,job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job =job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay *= (1.0+percent)

class Manager(Person):
    def giveRaise(self,percent,bonus=0.1):
        self.pay *= (1.0+percent+bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith',42,30000,'software')
    sue = Person('Sue Jones',45,40000,'hardware')
    tom = Manager('Tom Doe',50,50000)

    print(bob.lastName())
    print(sue.pay)
    sue.giveRaise(.10)
    print(sue.pay)
    print tom.pay
    tom.giveRaise(.10)
    print(tom.pay)