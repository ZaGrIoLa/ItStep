class Wolf:
  def Wolf(self):
        print("I am the strongest!")
        self.satiety=50
        self.stealth=10
        self.malice=50
class Fox(Wolf):
  def Wolf(self):
        print(self.satiety)
  def Fox(self):
        self.stealth=50
        self.malice=30
        print("I am the most stealth!")
class Hare(Fox):
  def Wolf(self):
        print(self.satiety)
  def Fox(self):
        print(self.stealth)
        self.malice=10
  def Here(self):
        print(f"Satiety={self.satiety}")
        print(f"Stealth={self.stealth}")
        print(f"Malice={self.malice}")

