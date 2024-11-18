dic1={1:10,6:30,4:20,2:60}
print("Dictionary is: ",dic1)

asc_val=sorted(dic1.items(),key=lambda x:x[1])
print("Ascending order of Values is: ",asc_val)

asc_Key=sorted(dic1.items(),key=lambda x:x[0])
print("Ascending order of Keys is: ",asc_Key)

desc_val=sorted(dic1.items(),key=lambda x:x[1],reverse=True)
print("Descending order of Values is: ",desc_val)

desc_Key=sorted(dic1.items(),key=lambda x:x[0],reverse=True)
print("Descending order of Keys is: ",desc_Key)
