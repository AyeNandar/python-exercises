states={'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
        }
cities={
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
        }
cities['NY']='New York'
cities['OR']='Portland'
print('_'*10)
print("NY State has:",cities['NY'])
print("OR State has:",cities['OR'])

print('_'*10)
print("Michigan's abberviation is:",states['Michigan'])
print("Florida's abbreviation is :",states['Florida'])


print('_'*10)
print("Mivhigan has:",cities[states['Michigan']])
print("Florida has :",cities[states['Florida']])
print('_'*10)
for state,abbrev in list(states.items()):
    print(state,"is abbreviated ",abbrev)
print("has city ",cities[abbrev])
print('_'*10)
state=states.get('Taxes')
if not state:
    print("Sorry ,no taxes.")
    city=cities.get('TX','Does Not exists')
    print("The city for the state 'TX' is :",city)

