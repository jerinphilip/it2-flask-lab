class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
        self.salary = 10000

    def get_name(self):
        return self.name

    def get_eid(self):
        return self.eid

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, eid, name):
        Employee.__init__(self, eid, name)
        self.salary = 100000
        self.vacation = False

    def go_on_vacation(self):
        self.vacation = True
        print('Yay')

class CEO(Manager):
    def __init__(self, eid, name):
        Manager.__init__(self, eid, name)
        self.salary = 10000000

    def make_strategy(self):
        print("Strategy")
