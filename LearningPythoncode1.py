# Session 1
# Create a python function that takes a user's first and last names and prints the user's full name.

first_name_str = 'Abraham'
last_name_str = 'Lincoln'

full_name_str = first_name_str + ' '+ last_name_str
print(full_name_str)

# String examples
'hello'
'hello' + ' world!'
'hello '*3
'hello '/3 # it will always have an error because you cannot subtract words

# Math Calculations
# Create Python code to convert temperatures in degrees Fahrenheit to Celsius: subtract 32 and multiply by 5/9"

celcius = 33.8
new_number_float= 5/9
fahrenheit_temp_int = 1

celsius_temp_int = (fahrenheit_temp_int - 32) * new_number_float
print(celsius_temp_int)

fahrenheit_temp_float = float(input('Please enter the amount in farenheit needed to change to celsius: '))
print((fahrenheit_temp_float - 32) * 5/9)

celsius_temp_float = float(input('Please enter the amount in celsius needed to change to fahrenheit: '))
print((celsius_temp_float + 32) * 9/5)

# Write Python code that takes years as input and prints out an estimated population (as an integer).
# Assume that the current population is 307,357,870 and assume that there are exactly 365 days in a year.

death_time_int = 13
new_immigrant_int = 35
current_population_int = 307357870
year_time_int = 365
hours_time_int= 24
minutes_time_int = 60
seconds_time_int = 60
birth_time_int = 45

seconds_year_int= year_time_int * hours_time_int * minutes_time_int * seconds_time_int
print(seconds_year_int)

print(seconds_year_int / birth_time_int)

population_year_int= (current_population_int + ((seconds_year_int/ birth_time_int) - (seconds_year_int/ death_time_int) + (seconds_time_int/ new_immigrant_int)))

birth_year_time = seconds_year_int / birth_time_int
death_year_time = seconds_year_int/ death_time_int
year_immigrant_int = seconds_time_int / new_immigrant_int
population_year_int = (current_population_int + birth_year_time - death_year_time + year_immigrant_int)

print(birth_year_time)
print(population_year_int)

# String examples

x="0123456789"

# display the element at position 0
x[0]

# display everything but the last element
x[:9]

# display the last element
x[9]

# display string "012345"
x[:6]

# display string "345678"
x[3:9]

# display only even numbers: "02468"  -- note use the Step
x[::2]

# display only odd numbers: "13579"  -- note use the Step
x[1::2]

# display the string in reverse order: "9876543210" -- note use the Step
x[::-1]
