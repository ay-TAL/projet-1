import nltk
from nltk.corpus import stopwords


try:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception:
    pass


MOTS_INUTILES = set(stopwords.words("french"))


def nettoyage(phrase):
    """Nettoie une phrase en masquant la ponctuation et filtrant les stopwords."""
    
    cleaner = phrase.replace("'", " ").replace("-", " ")
    
    mots_decoupes = [mot.lower().strip() for mot in nltk.word_tokenize(cleaner)]

    return [
        mot for mot in mots_decoupes 
        if mot.isalnum() and len(mot) > 1 and mot not in MOTS_INUTILES
    ]

try:
    with open("mon_fichier.txt", "r", encoding="utf-8") as fichier:
        for chaque_ligne in fichier:
            ligne_propre = nettoyage(chaque_ligne)
            if ligne_propre:
                print(ligne_propre)
except FileNotFoundError:
    print("Erreur : Le fichier 'mon_fichier.txt' est introuvable.")
