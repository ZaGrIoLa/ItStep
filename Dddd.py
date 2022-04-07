import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness=50
        self.progress=0
        self.scooter=0
        self.alive=True
    def to_study(self):
        print("Time to study!")
        self.gladness-=3
        self.progress+=0.12
    def to_sleep(self):
        print("Time to sleep")
        self.gladness+=3
    def to_chill(self):
        print("Rest time")
        self.gladness+=5
        self.progress-=0.1
    def to_drive(self):
        self.scooter = Scooter()

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive=False
        elif self.gladness <=0:
            print("Depression...")
            self.alive=False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive=False
    def end_of_day(self):
      print(f"Gladness={self.gladness}")
      print(f"Progress={self.progress,2}")


    def live(self, day):
      day="Day" + str(day) + "of" + self.name + "file"
      print(f"{day:=^50}")

      live_cube= random.randint(1,3)
      if live_cube==1:
        self.to_study()
      elif live_cube==2:
        self.to_sleep()
      elif live_cube==3:
        self.to_chill()
      self.end_of_day()
      self.is_alive()

class Scooter:
    def __init__(self):
        self.exersize=3
        self.speed=10
        self.resttime=5
    def to_exersizes(self):
        print("Time to exersize!")
        self.exersize+=1
        self.speed+=2
        self.resttime+=2
    def is_live(self):
        if self.exersize>=0:
            print("Time to exersise.Go home!")
            self.speed=0
    def printer(self):
        print(f"Speed={self.speed}")
        print(f"Exersize={self.exersize}")
        print(f"Resttime={self.resttime}")


sara= Student(name="Sara")
for day in range(365):
  if sara.alive==False:
    break
  sara.live(day)



