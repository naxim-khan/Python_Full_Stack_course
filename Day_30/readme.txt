Final Project of the Day.
topics: Errors, Exceptions and Saving JSON Data.

1. Handling Erros & Exceptions
example:

with open("data.txt" , "a") as file:
    data_file.write(f"{website}|{email}|{password}\n")
    website_entry.delete(0,END)
    password_entry.delete(0,END)

    lets if i make a type in the above instead of data.txt
    i write daata.txt and instead of the append mode i change instead of the
    append mode i change it to "r" (read)
    so in this case we will face an error 
    FileNotFoundError: No such file or directory: 'daata.txt'
    and as soon as this error happen it'll not execute the next lines codes.
so this the simple examples of error's in your program.
it can any type of error's for example a key error in dictionary 
key name errors ,index erorrs,type Errors of data types e.t.c.

=======:::Catching Exceptions:::=======
Rules:
try:
something that might cause an Exception
except:
Do this if there was an exception.
else:
Do this if there were no exceptions.
finally:
Do this no matter what happens
these are the four keywords which are more important when it comes to handling Exception

