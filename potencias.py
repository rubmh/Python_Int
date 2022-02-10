def pot(lim):
    count = 1
    while count <= lim:
        pot = count**2
        print(str(count) + " Elevado al cuadrado es: " + str(pot)  )
        count = count + 1 


def run():
    print("******************************************************************************")
    print("* Bienvenido                                                                 *")
    print("* Este programa te pondra las potencias                                      *")
    print("******************************************************************************")
    lim = int(input("Indica cuantas potencias quieres : "))
    pot(lim)
        


if __name__ == '__main__':  
    run()