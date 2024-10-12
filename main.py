print("Welcome!")
temp = float(input("Enter today's temperature in celsius (°C): "))

if temp >= 30: #assume a day with the temperature more than 30°C is considered a hot day
    print('''Today is a hot day
You can wear light and soft clothes.''')
    
else:
    print('''Today is a cold day
you should wear a jacket or a pullover to keep warm''')
    
