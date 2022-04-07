import random
class Human:
    def __init__(self, name="Human", job=None, home=None,car=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.job=job
        self.home=home
        self.car=car
    def get_home(self):
        self.home=House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=Job()
    def get_car(self):
        self.car=Auto()
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            pass
    def work(self):
        pass
    def shopping(self,manage):
        pass
    def chill(self):
        pass
    def to_repair (self):
        pass
    def clean_home (self):
        pass
    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand= random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strenght=brand_list[self.brand]["strenght"]
        self.consunption=brand_list[self.brand]["consunption"]
    brands_of_car={
        "BMW":{"fuel":100,"strenght":100,"consunption":6},
        "Lada":{"fuel":50,"strenght":40,"consunption":10},
        "Volvo":{"fuel":70,"strenght":150,"consunption":8},
        "Ferari":{"fuel":80,"strenght":120,"consunption":14},
    }
    def drive(self):
        if self.strenght>0 and self.fuel>=self.consunption:
           self.fuel = self.consunption
           self.strenght-=1
           return True
        else:
           print("The car can not move!")
           return False

class House:
    def __init__(self):
        self.ness=0
        self.food=0

class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]
        print(f"RRR={self.job}")

    job_list={
        "Java developer":{"salary":50, "gladness_less":10},
        "Python developer":{"salary":40, "gladness_less":3},
        "C++ developer":{"salary":45, "gladness_less":25},
        "Rust developer":{"salary":70, "gladness_less":1}
    }





