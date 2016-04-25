# coding: utf-8
from __future__ import unicode_literals

from PhS import *
import savReaderWriter

#########################################################################################################################
#                                                                                                                       #
# Le nom du fichier SPSS doit être strictement identique au nom du programme Python dont sont importées les données !!! #
#                                                                                                                       #
#########################################################################################################################

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

bdd = 'All Studies'
bdd = 'BdD_TestAncienneVersion'

tab = 'All_Studies_ByBrand'
#tab = 'All_Studies_ByBrandByCBR'
#tab = 'All_Studies_ByBrandByXp'

step = 1000000
step = 10

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# All_Studies_ByBrand      :  16.279.106 observations
# All_Studies_ByBrandByCBR :  30.791.795 observations
# All_Studies_ByBrandByXp  : 222.491.300 observations

nomfichiertexte = 'bdd_table.TXT'

# Nom du fichier de données SPSS 
SPSSFile = tab + '.sav'											
SPSSFile = tab + '_100premiers.sav'
# Récupération du dernier numéro d'identifiant
DernierIDFile = tab + '.txt'

def Nettoyage_Repertoire() :
	try : os.remove(tab + '.pyc')
	except : pass
	try : os.remove('Connection.pyc')
	except : pass
	try : os.remove(nomfichiertexte)
	except : pass
	exit()

# Création d'un fichier-texte pour récupération du nom de la base de données & du nom de la table
fichier_conn = open(nomfichiertexte, 'w')
try : fichier_conn.write(bdd)
except :
	print '\n Aucune base de données sélectionnée !\n'
	fichier_conn.close()
	Nettoyage_Repertoire()
try : fichier_conn.write('\n' + tab)
except :
	print '\n Aucune table sélectionnée !\n'
	fichier_conn.close()
	Nettoyage_Repertoire()
fichier_conn = open(nomfichiertexte, 'r')
fichier_conn.close()

# Importation de la connection & du curseur
from Connection import conn, cur

# Sélection des fichiers d'importation nécessaires à la création des tables correspondantes
Import_Tabl_Var = __import__(tab, globals(), locals(), (['Tables', 'Variables']))

clr()
#print '\n Base de donnée connectée...\n\n   * Base :', bdd, '\n\n   * Table :', tab, '\n\n'
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

# Création de la table de la base de données
Import_Tabl_Var.Tables(premier_id, tab)
if premier_id == 0 :
	conn.commit()
	print '\n Table de la base de données créée !'.encode('cp850')

# Boucle pour insertion des données
boucle = 0
while boucle < nb_boucles :
	Debut_Exec = Temps()
	boucle = boucle + 1
	print '\n Passage', boucle, '/', nb_boucles, ':\n'
	dernier_id = premier_id + step
	i_d = premier_id
	data = savReaderWriter.SavReader(SPSSFile, returnHeader=False, ioUtf8=True, ioLocale='french')
	# Insertion des données dans la table
	with data as reader :
		#allData = data.all()	# Si le PC encaisse... ce qui n'est pas le cas !
		for line in data[i_d:dernier_id] :		# Il faut "numpy" pour pouvoir utiliser des 'arrays' [...:...,...:...]
			i_d = i_d + 1
			pc = ( float(i_d - premier_id) / (dernier_id - premier_id) * 100 )
			try :
				# Insertion
				Import_Tabl_Var.Variables(i_d, tab, line)
				if pc == 100 : espace_pc = ''
				else : espace_pc = ' '
				if pc == int(pc / 10) * 10 : print ' Progression :', espace_pc, int(pc / 10) * 10, '%   [ ID :', Separe_Milliers(i_d, '.'), ']'
			except :
				print ( "\n Problème avec l'identifiant " + Separe_Milliers(i_d, '.') + "...   -   Exécution arrêtée !\n" ).encode('latin1')
				exit()
	conn.commit()
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

cur.close()
conn.close()
Nettoyage_Repertoire()



#data = savReaderWriter.SavReader(SPSSFile, returnHeader=True, ioLocale='french')
#with data :
#	allData = data.all()	# fetch all the data, if it fits into memory
#	print("The file contains %d records" % len(File))
#	print("The first six records look like this\n"), data[0:6]
#	print("The first record looks like this\n"), data[0]
#	print("The last four records look like this\n"), data.tail(4)
#	print("The last record looks like this\n"), data.tail(1)
#	print("The first five records look like this\n"), data.head()
#	print("First column:\n"), data[..., 0]	# requires numpy
#	print("Row 4 & 5, first three cols\n"), data[4:6, :3]	# requires numpy
