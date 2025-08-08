
# generate_password.py
import random
import string

def generate_password(length=12):
    """Génère un mot de passe aléatoire de la longueur spécifiée."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Générateur de mot de passe ===")
    print("Mot de passe (12 caractères) :", generate_password(12))
    print("Mot de passe (16 caractères) :", generate_password(16))
