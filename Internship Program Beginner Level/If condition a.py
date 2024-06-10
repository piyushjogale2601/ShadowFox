h=float(input("enter height in metres: "))
w=float(input("enter weight in kgs: "))
bmi=w/(h*h)

if bmi>=30:
  print(bmi, ", obesity")
elif bmi>=25 and bmi<=29:
  print(bmi, ", overweight")
elif bmi>=18.5 and bmi<=25:
  print(bmi, ", normal")
elif bmi<18.5:
  print(bmi, ", underweight")