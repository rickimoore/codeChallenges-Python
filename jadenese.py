# coding: utf-8
def toJadenCase(string):
    words = string.split()
    jadenese = []
    
    for word in words:
        jadenese.append(word.capitalize())
    
    return " ".join(jadenese)
