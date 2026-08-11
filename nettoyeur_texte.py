import nltk
from nltk.corpus import stopwords

mots_inutiles = set(stopwords.words("french"))

def nettoyage(phrase):

    liste = []
    mots_a_decouper = phrase.replace("'", " ")
    phrase_nettoyee = nltk.word_tokenize(mots_a_decouper)

    for word in phrase_nettoyee:
        texte = word.lower().strip()

        if texte.isalnum() and texte not in mots_inutiles:
            liste.append(texte)

    return liste


texte_test = input("Insérez votre texte : ")

resultat = nettoyage(texte_test)

print("\nLe résultat final de votre liste est :")
print(resultat)     
