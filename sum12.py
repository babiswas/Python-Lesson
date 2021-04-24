class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
     return f"{self.a} and {self.b}"

  def display_sum(self):
      return self.a+self.b

class B:
  def __init__(self,d,e):
      self.d=d
      self.e=e
  def __str__(self):
      return f"{self.d} and {self.e}"

  def display_sub(self):
      return self.d-self.e

class C(A,B):
   def __init__(self,a,b,c,d):
       A.__init__(self,a,b)
       B.__init__(self,c,d)
   def __str__(self):
       return f"{self.a} and {self.b} and {self.e} and {self.d}"
   def display_sum(self):
       print("Displaying parent class function")
       print(super().display_sum())
       return self.a+self.b+3
   def display_sub(self):
       print("Displaying parent class function")
       print(super().display_sub())
       return self.d-self.e+5
 

if __name__=="__main__":
  c=C(1,2,3,4)
  print(c)
  print(c.__dict__)
  print(c.display_sub())
  print(c.display_sum())
  print("Is c subclass of A")
  print(issubclass(C,A))
  print("Is c subclass of B")
  print(issubclass(C,B))
  print("Is A subclass of B")
  print(issubclass(A,C))
  

