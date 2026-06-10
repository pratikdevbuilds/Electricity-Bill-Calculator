get_unit=int(input("enter units : "))
if get_unit>100:
  f_100= get_unit-100
  pyment=100*5
  if f_100>100:
    re_100 =f_100-100
    pyment=pyment+(100*7)
    if re_100>0:
     pyment=pyment+(re_100*10)

  else:
    pyment=pyment+(f_100*7)

else:
  pyment=get_unit*5
 

print(f"TOTAL AMOUNT = {pyment} /-")
