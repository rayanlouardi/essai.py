def sécurité(vitesse, limite, récidive):
    """Voir si une personne conduit correctement
    Args :
    Vitesse (int) : voir à combien la personne conduit
    limite (int) : voir à combien est la limitation de vitesse
    récidive (bool) : voir si la personne a recommencé
        
    
    Returns :
    L'amende encourue, les points perdus, le nombre d'année de suspension de permis et combien de mois il ira en prison    """    

    dépassement = vitesse - limite
    if dépassement  == 0:
       res = (0, 0, 0, 0)
    elif dépassement == 20:
        if limite > 50:
            res = (68, 1, 0, 0)
        else:
            res = (135, 1, 0, 0)
    elif dépassement > 20 and dépassement <= 30:
        res = (135, 2, 0, 0)
    elif dépassement > 30 and dépassement <= 40:
        res = (135, 3, 3, 0)
    elif dépassement > 40 and dépassement <= 50:
        res = (135, 4, 3, 0)
    elif dépassement > 50:
        res = res(1500, 6, 3, 0)
    elif récidive == True and dépassement > 50:
        res = (3750, 6, 3, 6)
    return res


def test_sécurité():
    assert test_sécurité(70, 20, False) == (135, 4, 3, 0)
    assert test_sécurité(80, 90, False) == (0, 0, 0, 0)
    assert test_sécurité(130, 50, False) == (1500, 6, 3, 0)
    assert test_sécurité(130, 50, True) == (3750, 6, 3, 6)

"""v = int(input("Entrez la vitesse à laquelle vous rouliez : "))
l = int(input("Entrez à combien était la limite de vitesse : "))
r = bool(input("Précisez si vous avez récidivé : "))
print(sécurité(v, l, r))"""
