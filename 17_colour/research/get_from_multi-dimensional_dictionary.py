# Example of dict.get() with multidimensional dict 
dict = {'India': {'captain': 'Virat', 'Batsman': 'Rohit', 'Bolwer': 'Bumrah'}, 
        'England': {	'captain': 'Root', 'Batsman': 'Buttler', 'Bolwer': 'anderson'}, 
        'Australia': {'captain': 'Paine', 'Batsman': 'Warner', 'Bolwer': 'Starck'}, 
        'Pakistan': {'captain': 'Babar', 'Batsman': 'Hafiz', 'Bolwer': 'Aamir'}, 
        'West Indies': {'captain': 'Pollard', 'Batsman': 'Gayle', 'Bolwer': 'Narayan'} 
        } 
  
# find batsman for india 
# return Not Found if not exists in dict 
print(dict.get('India').get('Batsman', 'Not Found')) 

## this example returns an empty dictionary if the first key isn't found
## thereby avoiding an error and the halting of script execution.

# Example of dict.get() with multidimensional dict 
dict = {'India': {'captain': 'Virat', 'Batsman': 'Rohit', 'Bolwer': 'Bumrah'}, 
        'England': {'captain': 'Root', 'Batsman': 'Buttler', 'Bolwer': 'anderson'}, 
        'Australia': {'captain': 'Paine', 'Batsman': 'Warner', 'Bolwer': 'Starck'}, 
        'Pakistan': {'captain': 'Babar', 'Batsman': 'Hafiz', 'Bolwer': 'Aamir'}, 
        'West Indies': {'captain': 'Pollard', 'Batsman': 'Gayle', 'Bolwer': 'Narayan'} 
        } 
  
# find batsman for new zealand 
# return Not Found if not exists in dict 
## The {} becomes the return value of the first get()
## when 'new zealand' isn't found. If {} isn't return (first example above)
## a string would be returned. The second get() would yield an error
## because get() isn't a method for string.
print(dict.get('new zealand',{}).get('Batsman', 'Not Found'))

## another example of the same thing, but with a 3D dictionary

# use of dict.get() in multidimensional dictionary 
  
dict = {'emp1': {'Name': {'First Name': 'Joe', 'Last Name': 'tribiani'},  
                 'age': 32}, 
        'emp2': {'Name': {'First Name': 'Mark', 'Last Name': 'Adam'}, 
                 'age': 20}, 
        'emp3': {'Name': {'First Name': 'luci', 'Last Name': 'truk'}, 
                 'age': 47}, 
        } 
  
# return Not Found if emp2 is not found 
# or Name is not Found or Last name is not found 
print(dict.get('emp2', {}).get('Name', {}).get('Last Name', 
                                               'Not Found')) 
