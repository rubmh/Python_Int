def run():
    #Reducioendo codigo y haciendo ahora raiz cuadrada
    my_list = []
    for i in range(1, 20):
        my_list.append(i)

    odd = list(filter(lambda x: x%2 != 0, my_list))
    print(odd)



if __name__ == '__main__':  
    run()