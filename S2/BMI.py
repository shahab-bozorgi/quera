wh = int(input())
hi = float(input())

bmi = wh / (hi * hi)

print('%.2f' % bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5<= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")