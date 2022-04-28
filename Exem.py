import random
class I:
    def __init__(self, name):
        self.name = name
        self.sleeptime=100
        self.satiety=50
        self.lovetime=0
        self.study=0
        self.dance=0
        self.youtubechuk=0
        self.enragesister=0
        self.familytime=0
        self.alive=True
    def to_study(self):
        print("Time to study!")
        self.sleeptime-=2
        self.lovetime-=1
        self.satiety-=0.10
        self.study+=3
        self.dance-=0.03
        self.familytime-=0.2
        self.enragesister-=50
        self.youtubechuk+=0.4
    def to_eat(self):
        print("Time to eat!")
        self.satiety+=3
        self.sleeptime-=0.3
        self.lovetime+=0.1
        self.study-=0.3
        self.dance-=0.03
        self.youtubechuk+=30
        self.enragesister-=2
        self.familytime+=0.2
    def to_youtube(self):
        print("Youtube time")
        self.lovetime+=3
        self.youtubechuk+=10
        self.satiety+=0.1
        self.sleeptime-=0.1
        self.study+=0.1
        self.enragesister+=0.2
        self.familytime-=1
        self.dance-=0.01
    def to_dance(self):
        print("Time to dance!")
        self.dance+= 3
        self.study+=1
        self.familytime-=0.3
        self.sleeptime-=0.2
        self.satiety-=0.5
        self.enragesister-=5
        self.youtubechuk-=2
        self.lovetime+=1
    def to_energesister(self):
        print("Time to energe sister!")
        self.enragesister+=100
        self.dance+=0.3
        self.sleeptime-=0.3
        self.lovetime+=0.4
        self.satiety-=0.3
        self.study-=0.5
        self.familytime-=0.3
        self.youtubechuk-=0.2
    def to_sleep(self):
        print("Time to sleep!")
        self.sleeptime+=100
        self.study-=2
        self.lovetime+=2
        self.familytime-=3
        self.youtubechuk-=20
        self.enragesister-=30
        self.satiety-=20
        self.dance-=3
    def to_family(self):
        print("time to family!")
        self.familytime+=20
        self.sleeptime-=20
        self.dance-=3
        self.youtubechuk-=30
        self.satiety+=4
        self.enragesister+=2
        self.lovetime+=2
        self.study+=2
    def to_love(self):
        print("Love time!")
        self.lovetime+=3
        self.sleeptime+=0.4
        self.youtubechuk+=0.6
        self.satiety-=1
        self.dance+=3
        self.study-=3
        self.enragesister-=20
        self.familytime+=1
    def is_alive(self):
        if self.sleeptime < -0.5:
            print("Died...")
            self.alive=False
        elif self.satiety <=0:
            print("Died too...")
            self.alive=False
        elif self.lovetime < -0.5:
            print("Depresion...")
            self.alive=True
        elif self.study > 1:
            print("You are stupid...")
            self.alive=True
        elif self.dance > 1:
            print("you will soon be in the last line..")
            self.alive=True
        elif self.youtubechuk>1:
            print("Immediately")
            self.alive=True
        elif self.enragesister>10:
            print("She willeat you soon....Nooo")
            self.alive=False
        elif self.familytime>0:
            print("To take offense at you soon.....")
            self.alive=False
    def end_of_day(self):
      print(f"Satiety={self.satiety}")
      print(f"Sleeptime={self.sleeptime,2}")
      print(f"Lovetime={self.lovetime}")
      print(f"Study={self.study}")
      print(f"Dance={self.dance}")
      print(f"Youtubee={self.youtubechuk}")
      print(f"Energe sister={self.enragesister}")
      print(f"Family time={self.familytime}")
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
olya= I(name="Olya")
for day in range(365):
  if olya.alive==False:
    break
  olya.live(day)