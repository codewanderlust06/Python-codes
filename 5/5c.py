dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print("New Concatenatd Dictionary is: ",dic4)
print("Sum of values of dictionary is: ",sum(dic4.values()))
print("Sum of Keys of dictionary is: ",sum(dic4.keys()))
                                           
