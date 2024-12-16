maths=int(input('enter the marks for maths'))
chemistry=int(input('enter the marks for chemistry'))
physices=int(input('enter the marks for physices'))
total_marks=600
sum_marks=maths+chemistry+physices
per=(sum_marks/total_marks)*100
print(per)
if per<35:
    print('grade is F')
elif per>35 and per<=50:
    print('grade is c')
elif per in range(51,90):
    print('grade is b')
elif per in range(90,101):
    print('grade is a')
else:
    print('invalid per')    
