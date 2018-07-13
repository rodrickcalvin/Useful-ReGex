import re

# EXAMPLE 1 - SEARCHING
patterns = ['term1', 'term2', 'term3']

text = 'This is a string with term2, but not the other term.'

for pattern in patterns:
    print(f'Searching for {pattern} in text')

    # pattern, text
    if re.search(pattern, text):
        print('Match was found\n')
    else:
        print('No match Found\n')

match = re.search('term2', text)
print(match)
print(type(match))


# EXAMPLE 2 - SPLITTING
email = 'rodrickwamala@gmail.com'

split_at = '@'

print(re.split(split_at, email))

# EXAMPLE 3 - FINDING
print(re.findall('rod', 'The email rodrickwamala@gmail.com belongs to the user wamala rodrick and has a username rodcalvin.'))