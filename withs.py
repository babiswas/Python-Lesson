class A:
   def __init__(self,filename):
       self.filename=filename

   def __enter__(self):
       self.file=open(self.filename,'w')
       return self.file

   def __exit__(self,val1,val2,val3):
       self.file.close()

if __name__=="__main__":
   with A("test100.txt") as file:
      file.write("Hello World")
      file.write("Hi world")
      file.write("Bye world")

       