# coding=UTF-8
import re

persons = []

def create_person():
    name = input('name: ')
    if re.search('^(?![\W_]+$)\S{2,10}$', name):
        address = input('address: ')
        phone = input('phone: ')
    else:
        print("您输入的姓名超长了,请重新输入")
        return create_person()
    if re.search('^(?!\d+$)(?![\W_]+$)\S{10,}$', phone):
        person = {'name': name, 'address': address, 'phone': phone}
        persons.append(person)
    #if len(phone) == 1:
    else:
        print("您输入的手机号格式不正确,请重新输入")
        return create_person()
def list_person():
    for person in persons:
        print('%s,%s,%s' % (person['name'], person['address'], person['phone']))

def query_person():
    name = input('name: ')
    line = len(name)
    if len(name) == 2:
        print("名字过短,请重新输入")
        return query_person()
    else:
        for person in persons:
            if person['name'] == name:
                print('%s,%s,%s' % (person['name'], person['address'], person['phone']))
#def query_phone():
def delete_person():
    name = input('name: ')
    for person in persons:
        if person['name'] == name:
            persons.remove(person)
            break

def get_choice():
    print('1. create person')
    print('2. list all persons')
    print('3. query person')
    print('4. delete person')
    print('5. quit')
    choice = input('Enter a number(1-5):')
    return choice

def main():
    while True:
        choice = get_choice()

        if choice == '1':
            create_person()
        elif choice == '2':
            list_person()
        elif choice == '3':
            query_person()
        elif choice == '4':
            delete_person()
        elif choice == '5':
            break
        else:
            print('Invalid choice')
            break

main()
