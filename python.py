# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# 2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students[0])

# 3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

# 4 Change the value 20 in z to 30
z[0]['y'] = 30
print(z[0])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for student in some_list:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")
iterateDictionary(students)

# first name
def iterateDictionary2(key_name, some_list):
    for name1 in some_list:
        print(name1[key_name])
iterateDictionary2('first_name', students)

# last name
def iterateDictionary2(key_name, some_list):
    for name2 in some_list:
        print(name2[key_name])
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo(some_dict):
    print(len(some_dict['locations']), "locations".upper())
    for city in some_dict['locations']:
        print(city)
    print()
    print(len(some_dict['instructors']), "instructors".upper())
    for instructor in some_dict['instructors']:
        print(instructor)

printInfo(dojo)