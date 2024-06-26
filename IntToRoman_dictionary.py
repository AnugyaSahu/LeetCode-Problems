
"""
Given an integer, convert it to a Roman numeral.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating a dictionary with roman numerals in decreasing order
        r_dict = {1000:"M", 900:"CM", 500:"D",400:"CD",100:"C", 90:"XC",50:"L",40:"XL",10: "X",9:"IX",5:"V",4:"IV",1:"I"}
        result = ""
        for key, value in r_dict.items():
            # check if target is less than key value
            while key <= num:
                # add if less as a string
                result += value
                # subtract the key by target
                num -= key
        return result

