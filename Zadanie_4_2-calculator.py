import sys
import logging
logging.basicConfig(level=logging.DEBUG)

operation =input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

# Check if the operation is a number in range 1-4
def check_operation(operation):
    try:
        operation = int(operation)
        if operation not in [1,2,3,4]:
            logging.error("Podana wartość nie jest liczbą z zakresu 1-4!")
            exit(1)
        return operation
    except ValueError:
        logging.error("Podana wartość nie jest liczbą z zakresu 1-4!")
        exit(1)

operation = check_operation(operation)

# Check if the given input is a number and if so return it as a float
def check_given_number(number):
    try:
        number = float(number)
        return number
    except ValueError:
        logging.error("Podana wartość nie jest liczbą!")
        exit(1)

number1 = input("Podaj składnik 1. ")
number1 = check_given_number(number1)


number2 = input("Podaj składnik 2. ")   
number2 = check_given_number(number2)


# Perform the operation
if operation == 1:
    logging.debug("Dodaję %s i %s" % (number1, number2))
    result = number1 + number2
    
    print("Czy chcesz dodać więcej liczb? T/N")
    more_numbers = input()
    if more_numbers == "T" or more_numbers == "t":
        number3 = input("Podaj kolejne składniki dodawania oddzielone spacjami: ")
        numbers = number3.split()
        result_with_more_numbers = number1 + number2
        for number in numbers:
            number = check_given_number(number)
            logging.debug("Dodaję %s do poprzedniego wyniku %s" % (number, result_with_more_numbers))
            result_with_more_numbers = result_with_more_numbers + number
           
        print("Wynik to %s" % result_with_more_numbers)

    elif more_numbers == "N" or more_numbers == "n":            
        print("Wynik to %s" % result)
        
    else:
        logging.error("Nieprawidłowa wartość!")
        exit(1)
        
elif operation == 2:
    logging.debug("Odejmuję %s i %s" % (number1, number2))
    result = number1 - number2
    print("Wynik to %s" % result)
    
elif operation == 3:
    logging.debug("Mnożę %s i %s" % (number1, number2))
    result = number1 * number2
    
    print("Czy chcesz mnożyć więcej liczb? T/N")
    more_numbers = input()
    if more_numbers == "T" or more_numbers == "t":
        number3 = input("Podaj kolejne składniki mnożenia oddzielone spacjami: ")
        numbers = number3.split()
        result_with_more_numbers = number1 * number2
        for number in numbers:
            number = check_given_number(number)
            logging.debug("Mnożę poprzedni wynik %s przez %s" % (result_with_more_numbers, number))
            result_with_more_numbers = result_with_more_numbers * number
            
        print("Wynik to %s" % result_with_more_numbers)

    elif more_numbers == "N" or more_numbers == "n":            
        print("Wynik to %s" % result)
        
    else:
        logging.error("Nieprawidłowa wartość!")
        exit(1)
        
elif operation == 4:
    logging.debug("Dzielę %s i %s" % (number1, number2))
    result = number1 / number2
    print("Wynik to %s" % result) 
  
else:
    logging.error("Nie ma takiej operacji!")
    exit(1)