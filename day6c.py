count=0
total=0
attendance =[18,20,19,15,21]
for x in attendance:
    if x>=20:
        print ("FULL")
        count= count + 1
    
    else :
        print ("NOTFLL")
    total +=x
print(f'total attendance is {total}')
print(count)
