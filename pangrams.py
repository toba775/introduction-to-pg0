nums = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
num = input("enter a number")
for x in num:
    nums[x] += 1
print(nums)
pangram = True
for z in nums.values():
     if z == 0:
        pangram = False
if pangram == True:
    print("number is pangram")
else:
    print("number not pangram")





