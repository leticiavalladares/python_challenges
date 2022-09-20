# Knowing that 5 apples equals to 1 Kg
# Inout the amount of apples
# Ask if the weight needs to be in (k)KG or (l)lbs
# Calculate the weight of the apples

apple_g = 1000 / 5    # 200g

lb = 0.002205    # 1g -> 0.002205lb

apple_amount = int(input(f"Enter amount of apples: "))

unit = "empty"

while (unit != "l" or unit != "k"):
    unit = input(f"Do you want to know the weight in kg 'k' or lb 'l'?")
    if unit == "l":
        result = (int(apple_amount) * apple_g) * lb
        print(str(apple_amount) + f" apples weight " + str(result))
        break
    elif unit == "k":
        result = (int(apple_amount) * apple_g)
        print(str(apple_amount) + f" apples weight " + str(result))
        break
    else:
        print(f"Please enter 'k' or 'l'")


