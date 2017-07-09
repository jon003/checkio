#!/usr/bin/python3



def read_grille(cipher_grille, ciphered_password):
    result = ''
    for x_pos,x_data in enumerate(cipher_grille):
        for y_pos, y_data in enumerate(x_data):
            if cipher_grille[x_pos][y_pos] == 'X':
                result += ciphered_password[x_pos][y_pos]
    return result

def rotate_grille(cipher_grille):
    return list(zip(*cipher_grille[::-1]))
            
def recall_password(cipher_grille, ciphered_password):
    result = read_grille(cipher_grille, ciphered_password)
    cipher_grille = rotate_grille(cipher_grille)

    result += read_grille(cipher_grille, ciphered_password)
    cipher_grille = rotate_grille(cipher_grille)

    result += read_grille(cipher_grille, ciphered_password)
    cipher_grille = rotate_grille(cipher_grille)
    
    result += read_grille(cipher_grille, ciphered_password)
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

