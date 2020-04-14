<h1>Session 1</h1>

first_name_str = 'Abraham'
last_name_str = 'Lincoln'

full_name_str = first_name_str + ' '+ last_name_str
print(full_name_str)

# Math Calculations
celcius = 33.8
new_number_float= 5/9
fahrenheit_temp_int = 1

celsius_temp_int = (fahrenheit_temp_int - 32) * new_number_float
print(celsius_temp_int)

fahrenheit_temp_float = float(input('Please enter the amount in farenheit needed to change to celsius: '))
print((fahrenheit_temp_float - 32) * 5/9)

celsius_temp_float = float(input('Please enter the amount in celsius needed to change to fahrenheit: '))
print((celsius_temp_float + 32) * 9/5)


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
