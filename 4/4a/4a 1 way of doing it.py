l1=[10,20,30]
l2=[11,20,33]
for x in l1:
    if x in l2:
        print(True)
        break
else:
    print(False)
