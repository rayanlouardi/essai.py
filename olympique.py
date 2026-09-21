def qualification(genre, record, succès, champion_monde):
    """Voir si une personne est qualifié à l'épreuve d'athlétisme
    Args:
    record (int) : le temps mis au 100m inf à 12 pour homme ou 15 pour femme
    succès (int) : le nb de victoires au 100m qui doit être plus grand que 3
    genre (str)  : homme pour un homme ou femme pour une femme
    champion_monde (bool) : la personne a déjà été champion du monde
    
    Returns:
    La personne est qualifié"""

    res = False
    if champion_monde:
        res = True
    else:
        if succès >= 3:
            if genre == 'homme' and record < 12.0:
                res = True
            else:
                res = False
            if genre == 'femme' and record < 15.0:
                res = True
            else:
                res = False
    return res

def test_olympique():
    assert("homme", 10, 5, False) == True

LeRecord = int(input("Entrez votre record au 100m : "))
LeSuccès = int(input("Entrez votre nombre de victoire au 100m : "))
LeGenre = input("Entrez si vous êtes un homme ou une femme : ")
Champion = input("Precisez si vous avez déjà été champion du monde : ")
print(qualification(LeRecord, LeSuccès, LeGenre, Champion))







                