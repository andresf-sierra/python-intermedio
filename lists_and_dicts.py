def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}


    super_list=[
        {"firstname": "Rubiel", "lastname": "Sierra"},
        {"firstname": "Doris", "lastname": "Alvarez"},
        {"firstname": "Andres", "lastname": "Sierra"},
        {"firstname": "Jose", "lastname": "Sierra"},
        {"firstname": "Michael", "lastname": "Sierra"},
        {"firstname": "Elias", "lastname": "Sierra"},
    ]

    # for values in super_list:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')

    super_dict={
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()
