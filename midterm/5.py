kg=float(input("nhap kg: "))
m=float(input("nhap chieu cao: "))
bmi=kg/(m**2)
if bmi>=30:
    print("Ban dang qua thua can, can an uong lanh manh")
elif bmi >= 25 and bmi <=29.9:
    print("ban dang hoi thua can, can an uong lanh manh hon")
elif bmi >= 18.5 and bmi <=25:
    print("co the can doi")
else:
    print("ban hoi gay, can an boi bo them")
    
