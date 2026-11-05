readings = [22, 25, -5, 30, 150, 28, 35, 40, 0, 32]

clean_readings = [x for x in readings if 0 <= x <= 100]

fahrenheit = [(x * 9 / 5) + 32 for x in clean_readings]

alarm_minutes = [i for i, x in enumerate(clean_readings) if x > 35]

print("Original Readings:", readings)
print("Clean Readings:", clean_readings)
print("Temperature in Fahrenheit:", fahrenheit)
print("Alarm Minutes:", alarm_minutes)

high_readings = [x for x in clean_readings if x > 35]
print("High Readings:", high_readings)

reading_set = {x for x in clean_readings}
print("Unique Readings:", reading_set)

squared_readings = [x ** 2 for x in clean_readings]
print("Squared Readings:", squared_readings)

generator = (x for x in clean_readings)
print("Generator Values:", list(generator))