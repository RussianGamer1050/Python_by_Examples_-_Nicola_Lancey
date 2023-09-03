rain = str.lower(input("Is it raining outside? "))
if rain == 'yes':
    wind = str.lower(input("Is it windy? "))
    if wind == 'yes':
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
