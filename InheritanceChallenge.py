class Person:
    name = 'name'

class PersonAge(Person):
    age = 20


person = PersonAge()

print(person.age, person.name)
