"""
This file has 2 functions. The first one converts temperature from Fahrenheit to Celsius.
The second one classifies a temperature (in ºC) into 4 categories.
"""


"""
Convert temperature from Fahrenheit to Celsius.
    Parameter:
        temp_fahrenheit (float): temperature in °F
    Returns:
        float: temperature converted to °C
"""
# 1st: define the name of function, what it does and the variable (x).
def fahr_to_celsius(temp_fahrenheit):
# 2nd: write down the function and return the value.
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    return temp_celsius

"""
Classify a temperature (°C) into one of four categories.

    Categories:
        0 -> cold: (temp < -2)
        1 -> slippery: (-2 <= temp < 2)
        2 -> comfortable: (2 <= temp < 15)
        3 -> warm: (temp >= 15)

    Parameter:
        temp_celsius (float): Temperature in degrees Celsius.

    Returns:
        int: An integer code from 0 to 3 representing the temperature category.
"""
def temp_classifier(temp_celsius):
# Category 0: cold temperatures below -2°C
    if temp_celsius < -2:
        return 0
# Category 1: slippery temperatures between -2°C and 2°C
    elif -2 <= temp_celsius < 2:
        return 1
# Category 2: comfortable temperatures between 2°C and 15°C
    elif 2 <= temp_celsius < 15:
        return 2
 # Category 3: warm temperatures 15°C and above
    else:
        return 3
