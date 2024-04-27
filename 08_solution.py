#Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input('enter the password:')

P_length =len(password)

if P_length <6:
    strength = 'weak'
elif P_length <10:
    strength = 'medium'
else:
    strength = 'strong'

print(strength)