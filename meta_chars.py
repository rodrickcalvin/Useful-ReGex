# METACHARACTER_SYNTAX
import re
import Regular_Expressions

pattern1 = Regular_Expressions.patterns
text = Regular_Expressions.email


def multi_re_find(pattern1, text):
    """
    Takes in a list of regex patterns
    Prints a list of all matches
    """
    for pattern in pattern1:
        if True:
            print(f'Searching for {pattern}')
            print(re.findall(pattern, text))
            print('\n')


# Repetition Syntax
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

'''
For this section, comment out the repetition you don't need.
You can run one at a time ot give them different variable names.
I decided to use re-assigning of the variables.
'''

test_pattern = ['sd*']  # wherever the 's' is followed by zero or more d's
# test_pattern = ['sd+']  # wherever the 's' is followed by one or more d's
# test_pattern = ['sd?']  # wherever the 's' is followed by zero or one d
# test_pattern = ['sd{3}']  # wherever the 's' is followed by three d's
# test_pattern = ['sd{1,3}']  # wherever the 's' is followed by one or three d's

multi_re_find(test_pattern, test_phrase)

# CHARACTER SETS
test_pattern1 = ['[ds]']  # prints out either d's or s'
# test_pattern1 = ['s[sd]+']  # prints out either s' or d's bounded on the right-hand side of the s.

multi_re_find(test_pattern1, test_phrase)

# EXCLUSION(^) we use a character know as a caret
test_text = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!.,? @"]+', test_text))  # ------(***)

# The caret(^) in this context means exclusion or negation.
# The string will be printed in exclusion of all the punctuation and each word stored in a list.
# Note this:
# ---- Without the '+' sign, then each character in the string will be printed out in a list without the punctuations.
# ---- When its added, the string is printed in a way that the characters before and after the
#       punctuation are grouped together and placed as strings. try out each of the case in your console.

test_patterns = [
    '[a-z]+',  # sequences of lower case letters printed in a list.
    '[A-Z]+',  # sequences of upper case letters printed in a list.
    '[A-Za-z]+',  # sequences of both upper and lower case letters in a list. it is has a similar output as (***)
    '[A-Z][a-z]+'  # outputs any thing with an Upper case followed by lower case letters.
]

multi_re_find(test_patterns, test_text)

# ESCAPE CODES
# One can prefix with either a backward slash or an 'r'

test_prefix = 'This is a string with some numbers 123456789 and symbols #####'

test_pattern2 = [
    r'\d+',  # list of digit characters of the string
    r'\D+',  # list of non digit characters of the string
    r'\s+',  # list of whitespaces with in the string
    r'\S+',  # list of strings with no whitespaces
    r'\w+',  # list of alphanumeric characters
    r'\W+'  # list of non alphanumeric characters
]

multi_re_find(test_pattern2, test_prefix)
