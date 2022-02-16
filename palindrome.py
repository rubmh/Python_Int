def run():
    print("******************************************************************************")
    print("* Bienvenido                                                                 *")
    print("* Este programa te pondra las potenpalindromo con funciona lamda             *")
    print("******************************************************************************")
    read = input("cual es la palabra que quieres analizar : ")
    palindrome = lambda string: string == string[:: -1]
    if palindrome(read.upper()) == True:
        print(" La palabra " + read + " es un Palindromo " )

    else: 
        print(" La palabra " + read + " NO es un Palindromo ") 


if __name__ == '__main__':  
    run()