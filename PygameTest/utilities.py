def toRomanNumeral(num: int) -> str:
    if num == 0:
        return "Ø"
    romanNumeral = ""
    while num >= 1000:
        romanNumeral += "M"
        num -= 1000
    while num >= 500 and num < 900:
        romanNumeral += "D"
        num -= 500
    if num >= 900:
        romanNumeral += "CM"
        num -= 900
    while num >= 100 and num < 400:
        romanNumeral += "C"
        num -= 100
    if num >= 400:
        romanNumeral += "CD"
        num -= 400
    while num >= 50 and num < 90:
        romanNumeral += "L"
        num -= 50
    if num >= 90:
        romanNumeral += "XC"
        num -= 90
    while num >= 10 and num < 40:
        romanNumeral += "X"
        num -= 10
    if num >= 40:
        romanNumeral += "XL"
        num -= 40
    while num >= 5 and num < 9:
        romanNumeral += "V"
        num -= 5
    if num >= 9:
        romanNumeral += "IX"
        num -= 9
    while num >= 1 and num < 4:
        romanNumeral += "I"
        num -= 1
    if num >= 4:
        romanNumeral += "IV"
        num -= 4
    return romanNumeral

cursor = (
    "      XXX       ",
    "      X.X       ",
    "      X.X       ",
    "      X.X       ",
    "      XXX       ",
    "                ",
    "XXXXX XXX XXXXX ",
    "X...X X.X X...X ",
    "XXXXX XXX XXXXX ",
    "                ",
    "      XXX       ",
    "      X.X       ",
    "      X.X       ",
    "      X.X       ",
    "      XXX       ",
    "                ",
)