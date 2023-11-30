""" You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentences and calculate the number of letter in each words """
sentence="What is the Airspeed Velocity of an Unladen Swallow?"

result={word:len(word) for word in sentence.split()}

print(result)

  
