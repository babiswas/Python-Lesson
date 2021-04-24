from contextlib import contextmanager

@contextmanager
def process_file(filename):
   try:
     file=open(filename,'w')
     yield file
   finally:
     if file:
        file.close()

if __name__=="__main__":
   with process_file("Test1.txt") as file:
       file.write("hello world")
       file.write("Hi World")
       file.write("Good Boy")


      