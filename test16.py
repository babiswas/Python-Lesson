class A:
  def __init__(self,param1,**kwargs):
      self.param1=param1
      super().__init__(**kwargs)

  def __str__(self):
      return f"{self.param1}"

class C(A):
  def __init__(self,param2,**kwargs):
      self.param2=param2
      super().__init__(**kwargs)

  def __str__(self):
     return f"{self.param2}"

if __name__=="__main__":
   a=C(param1="hello",param2="bello")
   print(a)