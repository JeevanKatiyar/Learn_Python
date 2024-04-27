#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

#pet_species =  input('enter the pet species:')


age = int(input('enter the age:'))

if age <= 2 :
    pet = "dog"
elif age >= 5:
    pet = "Senior cat"
print(pet)
    