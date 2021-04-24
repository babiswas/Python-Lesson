from abc import ABC,abstractmethod

class A(ABC):
  def __init__(self,a,b):
      self.a=a
      self.b=b

  @abstractmethod
  def sum(self):
     pass

  @abstractmethod
  def sub(self):
     pass

class B(A):
   def __init__(self,b,c,d):
       super().__init__(b,c)
       self.d=d
   def sum(self):
      return self.a+self.b
   def sub(self):
      return self.a-self.b
   def display(self):
       return f"{self.d}"

if __name__=="__main__":
   b=B(2,3,4)
   print(b.sum())
   print(b.sub())
   print(b.display())
   k=A(2,3)
   
   
   