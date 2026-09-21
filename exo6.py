def algo1(a, b, c, d):
    """retrouver quel est la valeur la plus petite parmi a, b, c ,d
    Args ;
    a (float) : une valeur
    b (float) ; une valeur
    c (float) : une valeur
    d (float) : une valeur
    
    Returns :
    Le résultat le plus petit parmi les 4"""
    if a < b:
        res= a
    else:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

A = float(input("Donner moi une valeur pour a : "))
B = float(input("Donner moi une valeur pour b : "))
C = float(input("Donner moi une valeur pour C : "))
D = float(input("Donner moi une valeur pour D : "))
print(algo1(A, B, C, D))


def test_algo1():
    assert algo1(50, 450, 6666, 2) == 50 
    assert algo1(9, 10, 11, 12) == 9 




def algo2(mot):
    """Retrouver combien de fois les voyelles apparaîssent dans un mot
    Args:
    mot (str) = un mot
    
    Returns:
    Le nombre de fois qu'une lettre apparaît dans un mot"""

    res = 0
    for lettre in mot:
        if lettre in 'aeiouy':
            res = res + 1
        else:
            res = res - 1
    return res >= 0

m = str(input("Donner moi un mot : "))
print(algo2(m))


def test_algo2():
    assert algo2("rapidité") == True
    assert algo2("oui") == False



    

