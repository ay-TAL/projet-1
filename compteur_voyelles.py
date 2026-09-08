def compter_voyelles(texte: str) -> int:
    """
    Compte le nombre de voyelles présentes dans une chaîne de caractères.
    Prend en compte les minuscules et les accents français courants.
    """
    texte_propre = texte.lower().strip()
    liste_voyelles = ['a', 'e', 'i', 'o', 'u', 'y', 'é', 'è', 'à', 'ù', 'ô', 'û', 'î', 'ï', 'ë']
    compteur = 0
    
    for lettre in texte_propre:
        if lettre in liste_voyelles:
            print(f"Votre texte comporte la voyelle : {lettre}")
            compteur += 1
            
    return compteur

if __name__ == "__main__":
    mot_utilisateur = input("Veuillez saisir un mot ou une phrase : ")
    
    total_voyelles = compter_voyelles(mot_utilisateur)
    
    if total_voyelles == 0:
        print("Votre texte ne comporte aucune voyelle.")
    else:
        print(f"Votre texte comporte au total {total_voyelles} voyelles.")
