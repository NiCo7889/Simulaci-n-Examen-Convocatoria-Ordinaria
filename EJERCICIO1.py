def minion_game(banana):
    # your code goes here

    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    stuart = 0
    kevin = 0   
    for i in range(len(string)):
        palabra = string[i]
        if string[i] in 'AEIOU':
            kevin += len(string)-i
        else:
            stuart += len(string)-i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)