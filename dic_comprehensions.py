def run():
    #Reducioendo codigo y haciendo ahora raiz cuadrada
    my_dict = {i : round(i**0.5,4) for i in range(1, 1001) if i % 3 != 0}
    print(my_dict)  


if __name__ == '__main__':  
    run()