name = input("Enter your name:") #user input
# print(name) #output

print("HELLO",  name, ", or sunao")


person_A_name = input("What is your name:")
person_A_age = input("Enter your age in years:")

person_B_name = input("What is your name:")
person_B_age = input("Enter your age in years:")

if person_A_age > person_B_age:
    print(person_A_name, "is older than", person_B_name)
else:
    print(person_A_name, "is younger than", person_B_name)


# BMI calculator, ask name, weight and height?

# Ask for user information
person_name = input("What is your name? ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print(person_name, ", your BMI is: ", round(bmi, 2))
