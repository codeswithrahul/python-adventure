age = 22

# if age >= 18:
#     print("Can vote")
# else:
#     print("Can not vote")

print("can vote") if age >= 18 else print("can not vote")



# chaining comparison operator

age2 = 22

# if age2 >= 18 and age2 <= 28:
#     print("Eligible for exam")
# else:
#     print("Not Eligible for exam")

if 18 <= age2 <= 28:
    print("Eligible for exam")
else:
    print("Not Eligible for exam")