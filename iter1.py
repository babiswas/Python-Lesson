class A:
   def __init__(self,a):
       self.a=a

   def __str__(self):
      return f"{self.a}"

   def __iter__(self):
       self.b=10
       return self

   def __next__(self):
      if not hasattr(A,'b'):
         self.__iter__()
      if self.a>self.b:
         raise StopIteration
      temp=self.a
      self.a=self.a+1
      return temp

if __name__=="__main__":
   a=A(5)
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))

   
   
       