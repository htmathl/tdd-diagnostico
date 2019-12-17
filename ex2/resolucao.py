def trocar_vogais(x):

    letters = {
        "a": "@",
        "e": "&",
        "i": "!",
        "o": "#",
        "u": "*"
    }


    for l in letters:
        x = x.replace(l, letters[l])
    return x

print(trocar_vogais('luar')) 
# imprime l*@r

print(trocar_vogais('bocejo')) 
# imprime b#c&j#

print(trocar_vogais('tranquilo')) 
# imprime tr@nq*!l#

print(trocar_vogais('tédio')) 
# imprime téd!#

print(trocar_vogais('Amanhã')) 
# imprime Am@nhã
