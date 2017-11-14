# email slicing +++++++++++++++

word = 'Jacob Craig Ross and the Hounds from Hell.'

print (word[word.index('Hounds'):])
# prints 'Hounds from Hell'

# get user email
email = input('What is your email address?').strip() # strip function trashes any extra spcaes
# slice out user name
user = email[:email.index('@')]
# slice out domain name
domain = email[email.index('@') + 1 :]
# format message
output = 'Your username is {} and your domain name is {}'.format(user, domain)
# display output message
print (output)























# Security bot ++++++++++++++++

known_users = ['Jake', 'Sara', 'Cas', 'Gurt', 'Ozzy', 'Waffy', 'Buttercup', 'Puddintayne', 'Mucus']

print (len(known_users))
