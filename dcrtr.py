def decorator(func):
   print("decorator function called")
   def wrapper(*args,**kwargs):
       print("Wrapper function is called")
       return func(*args,**kwargs)
   return wrapper


def decorator1(func):
   print("decorator function called")
   def wrapper(*args,**kwargs):
       print("Wrapper function is called")
       return func
   return wrapper

@decorator1
def func1(*args,**kwargs):
  print(args)
  print(kwargs)

@decorator
def func(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

if __name__=="__main__":
   func(2,3,4,hello="bello",tello="mello")
   test=func1(4,5,6,4,tello="mello",kello="chillo")
   test(4,5,6,4,tello="mello",kello="chillo")
      