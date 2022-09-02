"""
lowercase
lowercase_with_underscores

naming: variables, function names, class attributes, class methods AND !file_names!

UPPERCASE
UPPERCASE_WITH_UNDERSCORES

naming: constants!

CamelCase

name: ClassNames!
"""

DATABASE_URL = 'postgres://abc:def@somehost.com:5432/dbname'
AVAILABLE_COLORS = ['white', 'green']
WEEKEND = [5, 6]


sum_ = 0
colors = ['red', 'blue', 'yellow']

for i in range(1, 100):
    sum_ += i

for colour in colors:
    print(colour)

# WEEKEND.append(4) atata ne mozhna!
# if current_day not in WEEKEND: days_counter += 1
