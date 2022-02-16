def run():
    my_list = []
    for i in range(1, 20):
        my_list.append(i)

    squares = list(map(lambda x: x**2, my_list))
    print(squares)



if __name__ == '__main__':  
    run()