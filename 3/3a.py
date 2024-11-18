def isPangram(sent1):
    st1="abcdefghijklmnopqrstuvwxyz"
    for s in st1:
        if s in sent1.lower():
            continue
        else:
            print("Sentence is NOT a pangram")
            break
    else:
        print("Sentence is a pangram")

sentence=input("Enter a sentence : ")
isPangram(sentence)
