#Weather Activity Suggestion
#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input('enter the weather:')

#activity= input('enter the activity to do:')

if weather == "Sunny":
    print('go for walk')
elif weather == "rainy":
    print('read a book') 
elif weather == "snowy":
    print('build a snowman')
else: 
    print('just sleep')