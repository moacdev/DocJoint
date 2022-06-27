
# coding=utf-8
import csv
from datetime import date
from random import random, randrange
import string
import time
from tkinter import filedialog
from unidecode import unidecode

kn=None
Fkn=None

f1 = filedialog.askopenfilename()
f2 = filedialog.askopenfilename()

fp = open(f1, 'r')
kn = csv.DictReader(fp, delimiter=';')
_kn = [ k for k in kn ]

with open(f2) as _fp:
    csv_file = csv.DictReader(_fp)
    esupn = [ cf for cf in csv_file ]
    counter=0
    for (krow) in _kn:
        kname = str(krow['Nom']).decode('utf-8').lower()
        knickname = str(krow['Pr\xc3\xa9nom']).decode('utf-8').lower()
        isOk = False
        for (row) in esupn:
            ename = str(dict(row)['\xef\xbb\xbfNom']).decode('utf-8').lower()
            enickname = str(dict(row)['Pr\xc3\xa9nom']).decode('utf-8').lower()
            if ( (unidecode(ename) == unidecode(kname) and unidecode(enickname) == unidecode(knickname) or unidecode(ename) == unidecode(knickname) and unidecode(enickname) == unidecode(kname) ) and dict(row)['Note/20,00'] != '-' ):
                # print( krow['Nom'] + ' : ' + dict(row)['Note/20,00'] )
                _kn[counter]['Note'] = dict(row)['Note/20,00']
                isOk = True
        if isOk == False: _kn[counter]['Note'] = 0
        isOk = False
        counter+=1
    print(_kn)

header=['Code Etudiant','Pr\xc3\xa9nom','Nom', 'Note']     
try:
   with open('output'+str(time.time())+'.csv',mode='w') as output_to_csv:
       dict_csv_writer = csv.DictWriter(output_to_csv, delimiter=';', fieldnames=header, dialect='excel')
       dict_csv_writer.writeheader()
       dict_csv_writer.writerows(_kn)
   print('\nData exported to csv succesfully and sample data')
except IOError as io:
    print('\n',io)