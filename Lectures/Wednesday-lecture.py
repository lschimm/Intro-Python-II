class Store:
    def __init__(self, name): # constructor
        self.name = name
        self.depts = [] # store has many departments

    def __str__(self):
        s =  f"Store: {self.name}\n"

        for n, d in enumerate(self.depts, start=1):
          s += f" {n}. {d.name}/n"
    
    def __repr__(self):
        return f"Store({repr(self.name)})"

    def add_dept(self, dept):
      self.depts.append(dept)
      print(self.depts)

class Dept:
  def __init__(self, name):
    self.name = name

  def __str__(self): # generally for human consumption
    return f"Dept: {self.name}"
  
  def __repr__(self): # generally for programmer consumption
    return f"Dept({repr(self.name)})"

# s is an object, an instance of Store
s = Store("Gundams R Us") # "instantiate" a new instance of class store
d = Dept("Schmoccer")

print(d)
s.add_dept(Dept("Schmokey"))
s.add_dept(Dept("Shmasketball"))
s.add_dept(Dept("Shmennis"))

# print(s)

num = input("Enter dept number: ")

i = int(num) - 1
print(f"\nYou selected department: {s.depts[1]}")