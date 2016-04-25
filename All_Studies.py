# coding: utf-8
from __future__ import unicode_literals
from PhS import *

import savReaderWriter

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

bdd = 'All Studies'

tab = 'All_Studies_ByBrand'
#tab = 'All_Studies_ByBrandByCBR'
#tab = 'All_Studies_ByBrandByXp'

# Pour info. :
# ------------
# All_Studies_ByBrand      :  16.279.106 observations
# All_Studies_ByBrandByCBR :  30.791.795 observations
# All_Studies_ByBrandByXp  : 222.491.300 observations

# Liste des variables dont la transformation de 'INTEGER' en 'BIGINT' est nécessaire (mettre [] si aucune variable à traiter)
Integer_vers_BigInt = ['ID']

step = 1000000

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Nom du fichier de données SPSS 
SPSSFile = tab + '.sav'											

# Récupération du dernier numéro d'identifiant
DernierIDFile = tab + '.txt'

def Nettoyage_Repertoire() :
	try :
		os.remove(tab + '.py')
		os.remove(tab + '.pyc')
	except : pass
	exit()

# Vérification de l'existence de la base de données
try :
	# Création & fermeture de la connection
	import psycopg2
	conn = psycopg2.connect(database=bdd, user='postgres', password='postgres', host='10.96.33.55', port='5432')
	conn.close()
except :
	print '\n Aucune base de données sélectionnée !\n'
	exit()

# Vérification de l'existence de la table
if os.path.isfile(SPSSFile) == False :
	print '\n Aucune table sélectionnée !\n'
	exit()

# Titre à l'écran
clr()
titre = '\n Base de donnée connectée...' + '\n' * 3
titre = titre + ' ╔' + '═' * (9 + len(bdd)) + '╗\n'
titre = titre + ' ║' + ' Base : ' + bdd    + ' ║\n'
titre = titre + ' ╚' + '═' * (9 + len(bdd)) + '╝\n\n'
titre = titre + ' ┌' + '─' * (10 + len(tab)) + '┐\n'
titre = titre + ' │' + ' Table : ' + tab    + ' │\n'
titre = titre + ' └' + '─' * (10 + len(tab)) + '┘\n'
print titre

# Récupération du dernier identifiant
try : dernier_id = open(DernierIDFile, 'r').read()
except :	# Le fichier-texte n'a pas encore été créé : on crée alors un fichier vide
	dernier_id = open(DernierIDFile, 'w')
	dernier_id = open(DernierIDFile, 'r').read()

# Demande du dernier identifiant pour savoir à partir duquel commencer ou reprendre
txt = ' à partir de (Idendifiant "moins" 1) : '
if dernier_id == '' : txt = '\n Commencer' + txt
else : txt = '\n Dernier identifiant : ' + Separe_Milliers(dernier_id, '.') + '\n\n Commencer/Reprendre' + txt
premier_id = raw_input(txt.encode('cp850'))

# Si rien n'est saisi, alors on reprend à partir du dernier identifiant par défaut
if len(premier_id) < 1 :
	premier_id = dernier_id
	# Il faut au moins saisir un nombre lors de la première exécution
	if dernier_id == '' :
		print "\n Il faut saisir un numéro d'identifiant au moins la première fois !...\n"
		os.remove(DernierIDFile)
		Nettoyage_Repertoire()
	else : print "\n Commence/Reprend après l'identifiant :", Separe_Milliers(premier_id, '.')
# Sinon on teste si la saisie est numérique
else :
	if premier_id.isdigit() == True : pass
	else : Nettoyage_Repertoire()
premier_id = int(premier_id)

# Demande d'exécution en boucle
exec_boucle = raw_input('\n Exécution en boucle ? (sur un pas de '.encode('cp850') + str(Separe_Milliers(step, '.')) + str(')  [ O / N ] '))
if exec_boucle == 'o' or exec_boucle == 'O' :
	txt = '\n Combien de passages doivent être effectués ? '
	nb_boucles = raw_input(txt.encode('cp850'))
	if nb_boucles.isdigit() == False : Nettoyage_Repertoire()
	else : pass
elif exec_boucle == 'n' or exec_boucle == 'N' : nb_boucles = 1
else : Nettoyage_Repertoire()
nb_boucles = int(nb_boucles)

# Création d'un fichier pour la création des fonctions 'Tables' & 'Variables'
fichier_fonctions = open(tab + '.py', 'w')

# Création de la connection & du curseur
fichier_fonctions.write('import psycopg2\n')
fichier_fonctions.write("conn = psycopg2.connect(database='" + bdd + "', user='postgres', password='postgres', host='10.96.33.55', port='5432')\n")
fichier_fonctions.write('cur = conn.cursor()\n')

# Fonction 'Tables' : création de la base de données
fichier_fonctions.write('\ndef Tables (premier_id, tab) :\n')
fichier_fonctions.write('\tif premier_id == 0 :\n')
fichier_fonctions.write("\t\tcur.execute('''\n")
fichier_fonctions.write("\t\t\tDROP TABLE IF EXISTS ''' + tab + ''';\n")
fichier_fonctions.write("\t\t\tCREATE TABLE IF NOT EXISTS ''' + tab + ''' (\n")
fichier_fonctions.write('\t\t\t\tI_d BIGINT NOT NULL PRIMARY KEY UNIQUE,\n')
import re
with savReaderWriter.SavHeaderReader(SPSSFile, ioUtf8=True, ioLocale='french') as header :
	# header.varNames			: list()
	# header.varLabels			: dict()
	# header.valueLabels		: dict() of dict()		
	# header.varNamesTypes		: tuple()
	# header.varNamesTypes[1]	: dict()
	# header.formats			: dict()
	nom_variables = header.varNames
	format_variables = header.formats
	for var in nom_variables :
		if   format_variables[var][:1] == "F"    : format = 'INTEGER'
		elif format_variables[var][:1] == "A"    : format = 'TEXT'
		elif format_variables[var][:4] == "DATE" : format = 'DATE'
		else :
			print '\nFormat inconnu !...\n'
			exit()
		if re.findall('F[0-9].+.', format_variables[var]) : format = 'REAL'
		if var in Integer_vers_BigInt : format = 'BIGINT'
		separateur = ','
		if var == nom_variables[len(nom_variables)-1] : separateur = ')'
		fichier_fonctions.write('\t' * 4 + var + ' ' + format + separateur + '\n')
fichier_fonctions.write("\t\t\t''')\n")
fichier_fonctions.write('\t\tconn.commit()\n')
fichier_fonctions.write("\t\tprint '\\n Table de la base de donn\\xe9es cr\\xe9\\xe9e !\\n'\n")

# Fonction 'Variables' : insertion des données dans la table créée
fichier_fonctions.write('\ndef Variables (i_d, tab, line) :\n')
fichier_fonctions.write("\tcur.execute( 'INSERT INTO ' + tab + '\\")
fichier_fonctions.write('\n')
insert_into = '\t\t(I_d,'
pourcent_s = '\t\tVALUES (%s,'
pour_line = '\t\t(i_d,'
i = 0
with savReaderWriter.SavHeaderReader(SPSSFile, ioUtf8=True, ioLocale='french') as header :
	for var in nom_variables :
		separateur_var = ','
		separateur_pourcent_s = ','
		separateur_pour_line = ','
		if var == nom_variables[len(nom_variables)-1] :
			separateur_var = ') \\'
			separateur_pourcent_s = ")', \\"
			separateur_pour_line = ') )'
		insert_into = insert_into + var + separateur_var
		pourcent_s = pourcent_s + '%s' + separateur_pourcent_s
		pour_line = pour_line + 'line[' + str(i) + ']' + separateur_pour_line
		i += 1
fichier_fonctions.write(insert_into)
fichier_fonctions.write('\n')
fichier_fonctions.write(pourcent_s)
fichier_fonctions.write('\n')
fichier_fonctions.write(pour_line)
fichier_fonctions.write('\n')

# Fermeture pour rendre possible l'utilisation du fichier créé
fichier_fonctions.close()

# Importation des fonctions créées
Import_Tabl_Var = __import__( tab, globals(), locals(), (['Tables', 'Variables']) )

# Création de la table
Import_Tabl_Var.Tables (premier_id, tab)

# Boucle pour insertion des données
boucle = 0
while boucle < nb_boucles :
	Debut_Exec = Temps()
	boucle = boucle + 1
	print '\n Passage', boucle, '/', nb_boucles, ':\n'
	dernier_id = premier_id + step
	i_d = premier_id
	data = savReaderWriter.SavReader(SPSSFile, returnHeader=False, ioUtf8=True, ioLocale='french')
	with data as reader :
		#allData = data.all()	# Si le PC encaisse... ce qui n'est pas le cas !
		for line in data[i_d:dernier_id] :		# Il faut "numpy" pour pouvoir utiliser des 'arrays' [...:...,...:...]
			i_d = i_d + 1
			pc = ( float(i_d - premier_id) / (dernier_id - premier_id) * 100 )
			try :
				# Insertion des données
				Import_Tabl_Var.Variables (i_d, tab, line)
				if pc == 100 : espace_pc = ''
				else : espace_pc = ' '
				if pc == int(pc / 10) * 10 : print ' Progression :', espace_pc, int(pc / 10) * 10, '%   [ ID :', Separe_Milliers(i_d, '.'), ']'
			except :
				print ( "\n Problème avec l'identifiant " + Separe_Milliers(i_d, '.') + "...   -   Exécution arrêtée !\n" ).encode('latin1')
				exit()
	Import_Tabl_Var.conn.commit()
	print '\n Fin de progression - Dernier identifiant :', Separe_Milliers(i_d, '.'), '\n'
	Fin_Exec = Temps()
	Chrono(Debut_Exec, Fin_Exec)
	# Temps d'affichage trop long sur la machine virtuelle :
	import socket
	if socket.gethostname() == 'PARD-D201GB5J' : print ' ' + '*' * ( Taille_x - 2 )
	# Mise en fichier du dernier identifiant
	fichier_dernier_id = open(DernierIDFile, 'w')
	fichier_dernier_id.write( str(dernier_id) )
	fichier_dernier_id.close()
	premier_id = dernier_id

Import_Tabl_Var.cur.close()
Import_Tabl_Var.conn.close()

Nettoyage_Repertoire()
