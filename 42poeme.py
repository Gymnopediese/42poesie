
import random
import sys

if len(sys.argv) < 2:
    print("Utilisation: python 42poeme.py <file>")
    exit(1)

file_path = sys.argv[1]

word_count = 0
valid = True

compliments = [
    "Un poème magnifique !",
    "Une œuvre d'art poétique !",
    "Une belle harmonie de mots !",
    "Une composition poétique exceptionnelle !",
    "Vous êtes un doux poète !",
    "Vos mots dansent avec grâce !",
    "Une mélodie poétique envoûtante !",
    "Vos vers sont une caresse pour l'âme !",
    "Une symphonie de mots !",
    "Un poème qui touche le cœur !",
    "Une œuvre poétique à couper le souffle !",
    "Vos mots sont une douce mélodie !",
    "Une poésie qui éveille les sens !",
    "Vos vers sont un enchantement !",
    "Une poésie qui illumine l'esprit !",
    "Vos mots sont une douce caresse !",
    "Une poésie qui danse dans l'air !",
    "Vos vers sont une douce mélodie !",
    "Une poésie qui chante la beauté !",
    "Vos mots sont une douce mélodie !",
    "Une poésie qui enchante l'âme !",
]

def print_error(error, line = -1):
    global valid
    # print the error red !!
    if line != -1:
        print(f"\033[91mErreur: {error}, ligne {line + 1}\033[0m")
    else:
        print(f"\033[91mErreur: {error}\033[0m")
    valid = False


try:
    
    if file_path.endswith('.42p') is False:
        print_error("Le fichier doit avoir l'extension .42p")
        exit(1)
    
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    lines = [line for line in lines if line.strip() != ""]  # Remove empty lines
    lcount = 0
    for line in lines:
        words = line.split(" ")
        
        if word_count == 0:
            if len(words) != 7 and len(words) != 6:
                print_error(f"Les lignes doivent contenir exclusivement 7 mots ou exclusivement 6 mots, actuellement : {len(words)} mots", lcount)
            else:
                word_count = len(words)
        elif len(words) != word_count:
            print_error(f"Les lignes doivent contenir {word_count} mots, actuellement : {len(words)}", lcount)
            
        if len(line) != 42:
            print_error("Chaque ligne doit contenir exactement 42 caractères", lcount)

        lcount += 1
    
    if not valid:
        print_error("Le poème n'est pas valide")
        exit(1)
    if (lcount != 6 and word_count == 7) or (lcount != 7 and word_count == 6) or lcount < 6 or lcount > 7:
        print_error("Le poème doit contenir 6 lignes de 7 mots ou 7 lignes de 6 mots", lcount)
        exit(1)
    print("\033[92mPoème valide !\033[0m")
    print(f"\033[92m{random.choice(compliments)}\033[0m")
    
except FileNotFoundError:
    print_error(f"File '{file_path}' not found")
    exit(1)

