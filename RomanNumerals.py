def toRomanNumerals(intIn):
    newInt = intIn
    roman = ""
    while (newInt >= 1000):
        roman += "M"
        newInt -= 1000
    while (newInt >= 500):
        if (newInt >= 900):
            roman += "CM"
            newInt -= 900
        else:
            roman += "D"
            newInt -= 500
    while (newInt >= 100):
        if (newInt >= 400):
            roman += "CD"
            newInt -= 400
        else:
            roman += "C"
            newInt -= 100
    while (newInt >= 50):
        if (newInt >= 90):
            roman += "XC"
            newInt -= 90
        else:
            roman += "L"
            newInt -= 50
    while (newInt >= 10):
        if (newInt >= 40):
            roman += "XL"
            newInt -= 40
        else:
            roman += "X"
            newInt -= 10
    while (newInt >= 5):
        if (newInt == 9):
            roman += "IX"
            newInt -= 9
        else:
            roman += "V"
            newInt -= 5
    while (newInt > 0):
        if (newInt == 4):
            roman += "IV"
            newInt -= 4
        else:
            roman += "I"
            newInt -= 1
    return roman

print (toRomanNumerals(500))
print (toRomanNumerals(1999))
print (toRomanNumerals(426))
