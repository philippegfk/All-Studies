# coding: utf-8

import psycopg2

# Récupération du nom de la base de données (pour connection de la base de données & création du curseur) & du nom de la table
nomfichiertexte = 'bdd_table.TXT'
fichier_conn = open(nomfichiertexte, 'r')
liste = list()
for line in fichier_conn : liste.append(line.rstrip())
fichier_conn.close()
bdd = liste[0]
tab = liste[1]

# Connection de la base de données & création du curseur
conn = psycopg2.connect(database=bdd, user='postgres', password='postgres', host='10.96.33.55', port='5432')
cur = conn.cursor()
