def run():

    #list comprehensions
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = [i for i in my_list if i%2 != 0]

    print(odd)


    #usando filter

    odd = list(filter(lambda x: x%2 !=0, my_list))

    print(odd)

if __name__ == '__main__':
    run()
