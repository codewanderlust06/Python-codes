ch1=input("Enter an alphabet = ")
def CheckVowels(ch2):
    ch2=ch2.upper()
    if ch2 in["A","E","I","O","U"]:
        return True
    else:
        return False
print(CheckVowels(ch1))
    
