def phone_combination(digits,index,current):
    
    if index==len(digits):
        print("".join(current))
        return 

    phone = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
    }

    letters = phone[digits[index]]

    for letter in letters:
        current.append(letter)
        phone_combination(digits,index +1 ,current)
        current.pop()

phone_combination("23", 0, [])