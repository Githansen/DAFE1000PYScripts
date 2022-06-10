 ## Returnerer estimatet av den deriverte
def main(funksjon, x):
    h = 10**(-10);
    return (funksjon(x+h)-funksjon(x-h))/(2*h)
