# class syntax ( class ClassName: )
# Class naming convention = (PascalCase)

# class User:
#     #Creating Constructor 
#     def __init__(self): # A special method normally used to initialize the attributes.
#         # this method would every time when declare your class
#         print("New User has been created.")
    

# # creating Class object
# user_1=User()
# # creating attribute of our class object (attribute is the things that the object will have.)
# user_1.id="001"
# user_1.name="Nazeem"
# print(user_1.name)
# user_2=User()
# user_2.id="002"
# user_2.name="Khan"
# print(user_2.name)
# Constructor: Allow us to understand what should happen
# when our object is being constructed. (also known as 
# initializing an object. )

# Now let's what's the rule of the class here:
class User:
    # When you create any object from that class you must have to 
    # provide the parameter's with every object other wise it'll give you an error.
    def __init__(self,user_id,user_name) :
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
    
    # How to define a function inside class
    def follow(self,user):
        user.followers+=1
        self.following +=1



user_1=User("001","Nazeem")
user_2=User("002","Khan")
# print(user_1.id,user_1.name)
# print(user_2.id,user_2.name)

# Now let's use our function here
# e.g: User 1 decided to follow user 2
user_1.follow(user_2)

print(f"{user_1.name} Follwer's {user_1.followers} Following {user_1.following}")
print(f"{user_2.name} Follwer's {user_2.followers} Following {user_2.following}")


