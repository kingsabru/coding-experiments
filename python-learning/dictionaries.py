def main():
    simple_dict = {'name': 'John', 'age': '30', 'city': 'New York'}
    derived_dict = simple_dict
    print(derived_dict)
    derived_dict['name'] = 'Jane'
    print(derived_dict)
    print(simple_dict)
    simple_dict['country'] = 'USA'
    print(derived_dict)


if __name__ == '__main__':
    main()