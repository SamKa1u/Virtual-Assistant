import numpy as np

def i_saturate(Dp,Dn,Lp,Ln,Nd,Na, Aqni2):
    term1 = Dp / (Lp * Nd)
    term2 = Dn / (Ln * Na)
    term = term1 + term2
    return term*Aqni2, term1, term2

def bias_voltage(i_sat):
    i = float(input("enter I:"))
    i_i_sat = i/i_sat
    # print("i/i_sat:",i_i_sat)
    log_i_i_sat = np.log(i_i_sat)
    # print("log_i_i_sat = ",log_i_i_sat)
    return .026*log_i_i_sat

def current_pn(Aqni2, term,v):
    i_pn = Aqni2*term*(np.exp(v/.026)-1)
    return i_pn


def isat():
    q = 1.602 * 10**-19

    a = float(input('Enter A*10^-4 cm^2: '))
    A = a*10**-4

    ni = float(input('Enter ni cm^-3: '))**float(input("exp:"))
    ni2 = ni**2

    Aqni2 = A*q*ni2
    print(Aqni2)

    Dp = float(input('Enter Dp cm^2/s: '))
    Dn = float(input('Enter Dn cm^2/s: '))

    lp = float(input('Enter Lp *10^-4 cm:  '))
    ln = float(input('Enter Ln *10^-4 cm: '))
    Lp = lp*10**-4
    Ln = ln*10**-4

    Na = float(input('Enter Na cm^-3: '))**float(input("exp:"))
    Nd = float(input('Enter Nd cm^-3: '))**float(input("exp:"))

    #display user inputs
    print("\nA: ", A, " cm^-3",
    "\nDn:", Dn, "cm^2/s Dp:", Dp, "cm^2/s",
    "\nLp:", Lp, "cm Ln:", Ln, "cm",
    "\nNa:", Na, "cm^-3 Nd:", Nd, "cm^-3")

    #display I_sat
    i_sat, term1, term2, = i_saturate(Dp, Dn, Lp, Ln, Nd, Na, Aqni2)
    print("I_sat:",i_sat)

    if str(input("solve for voltage(v) or currents(c)")) != "v":
        #display Ip and In
        v = float(input("enter V:"))
        i_p = current_pn(Aqni2, term1, v)
        i_n = current_pn(Aqni2, term2, v)
        print("i_p:",i_p,"i_n:", i_n, "I:",i_p+i_n)
    else:
        #display forward bias voltage
        print("forward bias voltage:",bias_voltage(i_sat))


if __name__ == "__main__":
    isat()