
# calculatrice.py

def addition(a, b):
    """Retourne la somme de a et b."""
    return a + b

def soustraction(a, b):
    """Retourne la différence entre a et b."""
    return a - b

def multiplication(a, b):
    """Retourne le produit de a et b."""
    return a * b

def division(a, b):
    """Retourne le quotient de a / b. Gestion de la division par zéro."""
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

if __name__ == "__main__":
    print("=== Calculatrice simple ===")
    print("2 + 3 =", addition(2, 3))
    print("5 - 2 =", soustraction(5, 2))
    print("4 * 3 =", multiplication(4, 3))
    print("10 / 2 =", division(10, 2))
    print("10 / 0 =", division(10, 0))
