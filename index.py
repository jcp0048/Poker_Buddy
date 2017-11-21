

userPot = {}

while True:
    color_of_chip = raw_input("Enter chip color: ")
    if (color_of_chip == ""): break
    value_of_chip= raw_input("Enter chip value: ")
    userPot[color_of_chip] = {} # creates second dictionary layer
    userPot[color_of_chip]["value"] = float(value_of_chip)
    chip_quantity = raw_input("Enter chip quantity: ")
    userPot[color_of_chip]["quantity"] = int(chip_quantity)

print (userPot)

def calculate_total_pot_value():
    pot_total = 0.0
    for chip in userPot.iteritems():
        print(chip[1]) #This is the dictionary
        pot_total += (chip[1]['value'] * chip[1]['quantity'])
    return pot_total

print(calculate_total_pot_value())
