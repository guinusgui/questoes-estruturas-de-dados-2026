import string

def tratamento(target:list[str]):

    remove_especiais = str.maketrans("", "", string.punctuation)
    remove_numeros = str.maketrans("","",string.digits)
    for i, each in enumerate(target):
        each = each.lower()
        each = each.translate(remove_especiais)
        each = each.translate(remove_numeros)
        each = each.strip()
        target[i] = each
        
        