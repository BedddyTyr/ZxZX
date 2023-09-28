# Mek samting
print("--------------------------------------------")
print("**** Welcome to Calorie Burn Calculator ****")
print("--------------------------------------------")

# Prompt
print(" Please enter the following")
wt = eval(input("\n Weight (in lbs): "))
ht = eval(input("\n Height (in cm) : "))
age = eval(input("\n Age            : "))

ft = (0.0328 * ht)

BMR = ((10 * wt) + (6.25 * ft) - (5 * age))

print()
print("--------------------------------------------")

print("What is your lifestyle?")
ls = int(input("\n 1| Sedentary"
               "\n 2| Moderately active"
               "\n 3| Very Active" 
               "\n"
               "\n Enter lifestyle number: "))

print()

# this is the recap
print("----------------- Results ------------------")
print("\n Weight", wt, "\n Height", ht, "\n Age", age)
print("\n Your BMR is: " + str(round(BMR, 2)))

if ls == 1:
    calorie1 = (BMR * 1.2)
    print(" You've got a long way to go, but you'll get there!")
    print(" You need to burn " + str(round(calorie1, 2)) + " " + "calories")

elif ls == 2:
    calorie2 = (BMR * 1.375)
    print(" You're there, you just need a bit more work to do.")
    print(" You need to burn " + str(round(calorie2, 2)) + " " + "calories")

elif ls == 3:
    calorie3 = (BMR * 1.55)
    print(" Your body is in good shape, Keep it healthy and fit!")
    print(" You need to burn " + str(round(calorie3, 2)) + " " + " calories")

else:
    print("Invalid input")

print("\n Go Get Burnin'!")
