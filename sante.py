def sante(taille, poids):
    """Permet de détecter un pb de santé en fonction de l'imc

    Args:
        taille (float): la taille de la personne en mètre
        poids (int): le poids de la personne en kg

    Returns:
        str: le pb éventuellement détecté
    """
    imc = poids / (taille * taille)
    if imc < 16.5:
        res = "Famine"
    elif imc < 18.5:
        res = "Maigreur"
    elif imc < 25:
        res = "Normal"
    elif imc<30:
        res = "Surpoids"
    else:
        res = "Obésité"
    return res

def test_sante():
    assert sante(1.8, 80) == "Normal"   #indique que sante(1.8, 80) doit retourner Normal
    assert sante(1.6, 67) == "Surpoids"
    assert sante(1.6, 150) == "Obésité"
    assert sante(1.75, 30) == "Famine"
    assert sante(1.80, 55) == "Maigreur"


"""print(sante(1.75,70))"""
laTaille = float(input("Donner une taille en mètre : "))
lePoids = int(input("Donner un poids en kilos : "))
print(sante(laTaille, lePoids))