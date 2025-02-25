class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        roman += "M" * (num // 1000)
        num %= 1000
        if num >= 900:
            roman += "CM"
            num -= 900
        elif num >= 500:
            roman += "D"
            num -= 500
        elif num >= 400:
            roman += "CD"
            num -= 400
        roman += "C" * (num // 100)
        num %= 100
        if num >= 90:
            roman += "XC"
            num -= 90
        elif num >= 50:
            roman += "L"
            num -= 50
        elif num >= 40:
            roman += "XL"
            num -= 40
        roman += "X" * (num // 10)
        num %= 10
        if num >= 9:
            roman += "IX"
            num -= 9
        elif num >= 5:
            roman += "V"
            num -= 5
        elif num >= 4:
            roman += "IV"
            num -= 4
        roman += "I" * num
        return roman