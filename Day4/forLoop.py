for num in range(0,5):
    print(f"{num}")
    
# # it will print 0 - 4

# for num in range(0,11,2):
#     print(f"{num}")
    
# # it will print ---> 2,4,6,8,10

for num in range(1,11):
    if num % 2 == 0:
        print(num)
# it will print ---> 2,4,6,8,10


for num in range(1,11):
    print(f"2 * {num} = {2*num}")
    # print(num)
    
cart = ["books","laptop"]
for items in cart:
    print(items)