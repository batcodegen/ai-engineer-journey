hours = [2, 1.5, 0, 3, 1, 2.5, 0.5]
totalhrs = 0
for h in hours:
    totalhrs = totalhrs + h 
    if h < 1 :
        print(f"{h}hr is Too little")
    elif h >= 1 and h <= 2 :
        print(f"{h}hrs is Good")
    else :
        print(f"{h}hrs is Great")

print(f"Total hours : {totalhrs}")
print(f"Average : {totalhrs/7}")

highest = hours[0]
for h in hours:
    if h > highest:
        highest = h
print(f"Highest : {highest}")