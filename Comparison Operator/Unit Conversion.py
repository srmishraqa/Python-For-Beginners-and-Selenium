# Enter your weight
# enter you are entering in kg or lbs
# after that it will give output in the other unit

weight = input("Enter your weight : ")
unit = input("Enter (L)bs or (K)gs : ")

if unit.upper() == "L":
    weight = int(weight) * 0.45
    print(f'{weight} KG')

elif unit.lower() == "k":
    weight = int(weight) / 0.45
    print(f'{weight} Lbs')
else:
    print("OOPS!!! can't process")