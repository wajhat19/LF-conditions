usd=0
age=int(input('enter the age'))
if age in range(18,31):
    usd=5
elif age in range (31,51):
    usd=20
elif age>50:
    usd=0
inr=usd*83
if usd>0:
    print(f'the ticket cost in {inr} INR.')
else:
    print('free ticket')                      