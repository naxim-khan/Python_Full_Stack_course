# 2. Reproduce the Bug
# if you encounter a bug more than once then it'll easy to find it.
# but if you encounter only it once then it become the real problem. 
# 2. Reproduce the Bug
# from random import randint
# dice_img=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
# dice_num=randint(1,6)
# print(dice_img[dice_num])

# There is a bug in the above function sometime it produce error
# saying the list index out or range.
# so the problem if actualy that list index start from 0 
# and we mentioned randint(1,6) so when the randint generate 6 then it show us the error.

# below is the solution
# 2. Reproduce the Bug
from random import randint
dice_img=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
dice_num=randint(0,5)
print(dice_img[dice_num])