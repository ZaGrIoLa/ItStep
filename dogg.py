import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.sleeptime=50
        self.satiety=0
        self.lovetime=0
        self.alive=True
    def to_sleep(self):
        print("Time to sleep!")
        self.sleeptime+=3
        self.lovetime+=0.12
        self.satiety-=0.10
    def to_eat(self):
        print("Time to eat!")
        self.satiety+=3
        self.sleeptime-=0.3
        self.lovetime-=0.1
    def to_love(self):
        print("Love time")
        self.lovetime+=3

        self.satiety-=0.1
        self.sleeptime-=0.1
    def is_alive(self):
        if self.sleeptime < -0.5:
            print("Died...")
            self.alive=False
        elif self.lovetime <=0:
            print("Depression...")
            self.alive=False
        elif self.satiety < -0.5:
            print("Died too...")
            self.alive=False
    def end_of_day(self):
      print(f"Satiety={self.satiety}")
      print(f"Sleeptime={self.sleeptime,2}")
    def live(self, day):
      day="Day" + str(day) + "of" + self.name + "file"
      print(f"{day:=^50}")
      live_cube= random.randint(1,3)
      if live_cube==1:
        self.to_eat()
      elif live_cube==2:
        self.to_sleep()
      elif live_cube==3:
        self.to_love()
      self.end_of_day()
      self.is_alive()
milly= Dog(name="Milly")
for day in range(365):
  if milly.alive==False:
    break
  milly.live(day)