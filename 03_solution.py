#Grade Calculator
#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

#st_name = input('enter the name of the student:')

score = int(input('enter the score:'))

if score >=101:
    print('wrong grading')
    exit() # to exit the program.

if  score >= 90:
    print("A grade", score) 
elif score >=80:
    print("B grade", score)
elif score >=70:
    print("C grade", score)
elif score >=60:
    print("D grade")
else: print('fail')