age = 20
if age >= 18:
    print("You are eligible for voting in upcoming general election")

temp = 25
if temp > 30:
    print ("It's hot outside")
else:
    print("its' not hot")

score = 92
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print("Your Gade is:", grade)


fruits = ["apple", "orange", "banana"]

for f in fruits:
    print (f)

x = 0
while x<5:
    print (x)
    x+=1


for i in range(3):
    for j in range(3):
        print (i,j)
        j=j+1
    i=i+1
    print(i,j)
