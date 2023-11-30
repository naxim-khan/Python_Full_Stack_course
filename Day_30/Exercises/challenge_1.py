fruits = ["Apple","Pear","Orange"]
# Todo: catch the exception and make sure the code runs without crashing.

def make_pie(index):
    global fruits
    try:
        fruits=fruits[index]
        print(fruits+"pie")
    except IndexError:
        num=len(fruits)
        # num -= 1
        index = num
        for _ in range(0,index):
            print(f"{fruits[_]}+ pie")
    
        
        
        
        
        
        
        

make_pie(4)
