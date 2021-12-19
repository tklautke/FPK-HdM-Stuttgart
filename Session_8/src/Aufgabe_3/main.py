import what_am_i as wai
import random as random
liste = ['Hi', 13, 'Jo', 'Ichbins', 35, 'Banane', 'Kevin', 35, '17', 'Kamera']

random.shuffle(liste)

for index in range(len(liste)):
    wai.was_bin_ich(liste[index])