import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.sleeptime=50
        self.satiety=0
        self.lovetime=0
        self.play=0
        self.training=0
        self.mind=0
        self.alive=True
    def to_sleep(self):
        print("Time to sleep!")
        self.sleeptime+=3
        self.lovetime+=0.12
        self.satiety-=0.10
        self.mind+=0.03
        self.training-=0.03
    def to_eat(self):
        print("Time to eat!")
        self.satiety+=3
        self.sleeptime-=0.3
        self.lovetime-=0.1
        self.mind+=0.3
        self.training+=0.03
    def to_love(self):
        print("Love time")
        self.lovetime+=3
        self.play+=1
        self.satiety-=0.1
        self.sleeptime-=0.1
        self.mind+=0.01
    def to_training(self):
        print("Time to trainyng!")
        self.training+= 3
        self.mind+=0.5
        self.play+=0.3
        self.sleeptime-=0.2
        self.satiety-=0.5
    def to_play(self):
        print("Time to play!")
        self.play+=3
        self.training+=0.3
        self.sleeptime-=0.3
        self.lovetime-=0.3
        self.satiety-=0.3
        self.mind+=0.5
    def is_alive(self):
        if self.sleeptime < -0.5:
            print("Died...")
            self.alive=False
        elif self.lovetime <=0:
            print("Depression...")
            self.alive=True
        elif self.satiety < -0.5:
            print("Died too...")
            self.alive=False
        elif self.mind > 1:
            print("Stupid...")
            self.alive=True
        elif self.play > 1:
            print("Sadly..")
            self.alive=True
    def end_of_day(self):
      print(f"Satiety={self.satiety}")
      print(f"Sleeptime={self.sleeptime,2}")
      print(f"Lovetime={self.lovetime}")
      print(f"Play={self.play}")
      print(f"Training={self.training}")
      print(f"Mind={self.mind}")
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
fancy= Dog(name="Fancy")
for day in range(365):
  if fancy.alive==False:
    break
  fancy.live(day)