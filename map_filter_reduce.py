from functools import reduce
import json
class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   l=[A(1,2),A(3,4),A(5,6)]
   for obj in l:
      print(obj)
   print(list(map(lambda obj:obj.__dict__,l)))
   print(reduce(lambda obj1,obj2:str(obj1)+' '+str(obj2),l))
   print([str(obj) for obj in list(filter(lambda obj1:obj1.a>2,l))])
   for obj in l:
    print(json.dumps(obj.__dict__))