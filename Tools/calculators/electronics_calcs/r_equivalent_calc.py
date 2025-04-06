import numpy as np

"""
Calculates R equivalent from given R1 and R2
    Args:
        c (str): The relationship between the resistors parallel/ series 
    Returns:
        result (float): The result of the R equivalent calculation
"""
def Req(c):
    result = "NaN"
    #handle series case
    if c == "s":
        # R1
        a = float(input("resistor 1:"))
        # R2
        b = float(input("resistor 2:"))
        result = a + b

    #handle parallel case
    elif c == "p":
        # R1
        a = float(input("resistor 1:"))
        # R2
        b = float(input("resistor 2:"))
        rcpA = np.reciprocal(a)
        # print(rcpA)
        rcpB = np.reciprocal(b)
        # print(rcpB)
        r_eq = rcpA + rcpB
        result = np.reciprocal(r_eq)

    #handle invalid response
    else:
        print("enter valid response\n")
    return result

def Requivalent():
    on = True
    while on:
        #series or parallel
        c = str(input("series(s) or parallel(p):"))
        #call R equivalent function
        result = Req(c)
        #if result is valid print result
        if result != "NaN":
            print("The Req is : ",result,"\n\n")
            d = 0
            #prompt user to continue
            while d != 'y' and d != 'n':    #while response is invalid keep asking
                d = str(input("another?(y/n):"))
                if d == "y":
                    continue
                elif d == "n":
                    on = False
                    break
                else:
                    print("enter valid response\n")






"""
Calculates R equivalent from LLM provided R1, R2, and resistor configuration
    Args:
        c (str): The relationship between the resistors parallel/ series, 
        a (float): The value of resistor one, 
        b (float): The value of resistor two 
    Returns:
        result (float): The result of the R equivalent calculation
"""
def Req_0_5(c, a, b):
    result = "NaN"
    #handle series case
    if c == "series":
        result = a + b

    #handle parallel case
    elif c == "parallel":
        rcpA = np.reciprocal(a)
        # print(rcpA)
        rcpB = np.reciprocal(b)
        # print(rcpB)
        r_eq = rcpA + rcpB
        result = np.reciprocal(r_eq)

    #handle invalid response
    else:
        print("Error: resistor config could not be determined\n")

    return result

def Requivalent_0_5(r1,r2, config):
    on = True
    # call R equivalent function
    result = Req_0_5(config, float(r1), float(r2))
    while on:
        #if result is valid print result
        if isinstance(result, float):
            print("The Req is : ",result,"\n\n")
            d = 0
            #prompt user to continue
            while d != 'y' and d != 'n':    #while response is invalid keep asking
                d = str(input("another?(y/n):"))
                if d == "y":
                    config = str(input("Resistor configuration: "))
                    r1 = float(input("R1 value: "))
                    r2 = float(input("R2 value: "))
                    result = Req_0_5(config, float(r1), float(r2))
                    continue
                elif d == "n":
                    on = False
                    break
                else:
                    print("enter valid response\n")
        else:
            break


if __name__ == "__main__":
    Requivalent_0_5(1, 1, "series")