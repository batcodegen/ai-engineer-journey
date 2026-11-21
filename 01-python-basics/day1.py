name = "Prakhar"
city = "Indore"
role = "CEO of indiekart company"
years = 2
years = years + 1
hours = 1.5
print(f"{name} has {years} years")
if years >= 5:
    print("Senior")
else:
    print(f"{name} is started with company - {role} with an annual turnover of ₹{years}00 crore")
print("done")
if hours < 1:
    print("Too little")
elif hours >= 1 and hours <= 2 :
    print("Good")
elif hours > 2 :
    print("Great")