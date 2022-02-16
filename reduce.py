from functools import reduce

def run():
    my_list = []
    for i in range(1, 6):
        my_list.append(2)

    all_mult = reduce(lambda x, y : x * y, my_list)
    print(all_mult)



if __name__ == '__main__':  
    run()