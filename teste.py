#!/usr/bin/python
import csv

tipos = ['red', 'white', 'vinho'] 
with open('BaseWine_Red_e_White.csv', 'rw') as f:
    data = csv.reader(f, delimiter=';')
    for l in data:
        if l[13].lower() in tipos:
            pass
        else:
            print('ERROR ######### FUUUU')
