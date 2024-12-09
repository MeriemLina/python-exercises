def temperature_check(temp):
    if temp < 0:
        print("It's freezing!")
    if temp < 10:
        print("It's cold!")
    if temp < 20:
        print("It's cool!")
    print("Stay safe!")

temperature = int(input('please type in the temperature : '))
temperature_check(temperature)