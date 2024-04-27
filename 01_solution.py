#  Age Group Categorization
#Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input('enter the age: \n'))

if age <=13:
    print('child')
elif  13 <= age <= 19:
    print('teenage')
elif  20 <= age <= 59:
    print('adult')
else: print('senior')
