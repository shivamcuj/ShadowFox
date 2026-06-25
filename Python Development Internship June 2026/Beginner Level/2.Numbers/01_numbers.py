# This function takes a number and a format specifier as input and returns the formatted number as a string.
def format_number(number, specifier): 
    result = format(number, specifier) # Format the number with the given specifier
    return f'result = {result}'

print(format_number(221, 'o')) #'o' in python formatting stand for Octal