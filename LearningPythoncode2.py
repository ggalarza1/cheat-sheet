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
    
