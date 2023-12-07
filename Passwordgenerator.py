
import secrets
import string
# String constants for password generation 

alphabets = string.ascii_letters

numbers = string.digits

specialchars = string.punctuation
# Concatenating all possible characters 

secretText = alphabets + numbers + specialchars

# Password length 

passwordLen = 10


# Generating a random password 

secretPassword = ''

for count in range(passwordLen):

 secretPassword += ''.join(secrets.choice(secretText))

# Printing the generated password 

print("Your secret password is: " + secretPassword)

# Adding constraints for a more secure password 

while True:

 secretPassword = ''
 for count in range(passwordLen):

  secretPassword += ''.join(secrets.choice(secretText))

 if(sum(c in specialchars for c in secretPassword) >= 2 and
    
 sum(c in numbers for c in secretPassword) >= 2):

  break

# Printing the more secure password 

print("The secret password which is more secure: " + secretPassword)


