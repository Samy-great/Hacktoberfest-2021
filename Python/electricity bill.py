pr=int(input("Enter Previous Reading : "))
cr=int(input("Enter Current Reading : "))
r=cr-pr

bill=0.0

if(r<=100):
    bill=3.10*r
elif(r>=101 and r<=150):
    bill=100*3.10 + (r-100)*3.83
elif(r>=151 and r<=200):
    bill=100*3.10 + 50*3.83 + (r-150)*4.95
else:
    bill=100*3.10 + 50*3.83 + 50*4.95 +(r-200)*6.10

scharge= bill*0.2
fbill=bill+scharge
print("---------------------------------------")
print("Your Reading for this month is ",r)
print("Bill is Rs.:",round(bill))
print("Surcharge is Rs. : ",round(scharge))
print("Your Final  Bill Amount of this month is Rs. : ",round(fbill))
