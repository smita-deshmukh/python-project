age = int(input("Enter your age :"))

if age < 0 or age > 100:
    print("Invalid age")

elif age >= 18:
    print("Eligible for voting")

else:
    print("Not eligible for voting")