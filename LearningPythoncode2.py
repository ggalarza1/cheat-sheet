#Session 2
#Create a script that prompts the user for a grade percentage (Number from 0 to 100).
#If percentage is between 90 and 100, then inform the student he/she received an A.
#If percentage is between 80 and 90 (not included), then inform the student he/she received a B.
#If percentage is between 70 and 80 (not included), then inform the student he/she received a C.
#If percentage is between 60 and 70 (not included), then inform the student he/she received a D.
#Any other percentages - inform the student that they did not pass.

grade_percentage_float = float(input('Please enter your grade: '))
if grade_percentage_float <= 59:
    print('Failed')
elif 60 < grade_percentage_float <= 70:
    print('D')
elif 71 < grade_percentage_float <= 80:
    print('C')
elif 81 < grade_percentage_float <= 90:
    print('B')
else:
    print('A')

#Another "If" statement with else continued
first_name = 'Luigi'

if first_name == 'John':
    print('Hi John, nice to meet you')
else:
    print('I don''t know your name')

#Suitecase example
suitcase_weight_float = float(input('Please enter suitcase weight in pounds: '))
if suitcase_weight_float >= 50:
    print('There is an extra $25 dollars charge')
else:
    print('There is no extra charge')

# Creating an amortization schedule using Python

    from amortization.schedule import amortization_schedule

for number, amount, interest, principal, balance in amortization_schedule(150000, 0.1, 36):
    print(number, amount, interest, principal, balance)
