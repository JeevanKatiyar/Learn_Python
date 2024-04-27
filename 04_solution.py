#Fruit Ripeness Checker
#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input('enter the fruit :')
color = input('enter the color :')

if fruit == 'banana':
    if color == 'green':
        print('unripe')
    elif color == 'yellow':
        print('ripe')
    elif color == 'brown':
        print('overripe')

else: print('No information of this fruit')