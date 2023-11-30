import math 
def isEven(num):
        return math.remainder(num,2)==0
if __name__=="__main__":
    n=int(input().strip())
    even=isEven(n)
    if not even:
          print('Weird')
    elif not even and range (2,5):
          print('Weird')
    elif  even and range(6,20):
          print('Weird')        
    elif  not even and n>20:
          print('Weird')
    else:
          print('Not Weird')

          
    