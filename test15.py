class A:
  def __init__(self,a,b,**kwargs):
      print("Class A initiallised")
      self.a=a
      self.b=b
      super().__init__(**kwargs)
      print("Class A initiallisation done")

  def __str__(self):
      return f"{self.a} and {self.b}"

  def display_a(self):
      return f"{self.a} and {self.b}"

class C:
   def __init__(self,c,d,**kwargs):
      print("Class C initiallised")
      self.c=c
      self.d=d
      super().__init__(**kwargs)
      print("class c initiallisation done")

   def __str__(self):
      return f"{self.c} and {self.d}"

   def display_c(self):
       return f"{self.c} and {self.d}"


class D(A,C):
   def __init__(self,e,**kwargs):
       print("Class D initiallised")
       super().__init__(**kwargs)
       self.e=e
       print("Class D initiallisation done")

   def __str__(self):
      return f"{self.e} is e,{self.b} is b,{self.a} is a,{self.d} is d,{self.c} is c"

if __name__=="__main__":
   d=D(a=12,b=13,c=14,d=15,e=16)
   print(d)
   d.display_c()
   d.display_a()

   