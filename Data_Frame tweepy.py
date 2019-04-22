# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:54:23 2019

@author: MyComputer
"""


import tweepy
import pandas as pd

ckey= ''
csecret= ''
atoken=''
asecret=''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api =tweepy.API(auth)


#Dans ce tutoriel, je vais vous montrer un moyen simple de récupérer des 
#tweets sur Twitter en utilisant l'API de Twitter.
#Nous allons chercher des tweets,et les stocker dans un DataFrame


#Je vais commencer par créer un DataFrame vide avec les colonnes dont nous aurons besoin.
# on va utiliser la methode DataFrame du bib Pandas

df = pd.DataFrame(columns = ['Tweets', 'User', 'User_statuses_count', 
                             'user_followers', 'User_location', 'User_verified',
                             'rt_count', 'tweet_date'])

#Ensuite, je vais définir une fonction comme suit.
def stream(data, file_name):
    i = 0
    #count=100 c'est le nombre de tweet a retourner via le api.search
    #lang='en' Ici, je filtre les résultats pour renvoyer les tweets en anglais uniquement.
    
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():
        
        #Ensuite, je remplis mon DataFrame avec les attributs qui m'intéressent 
        #et lors de chaque itération en utilisant la méthode .loc du bib Pandas et mon compteur i.
        df.loc[i, 'Tweets'] = tweet.text
        df.loc[i, 'User'] = tweet.user.name
        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df.loc[i, 'user_followers'] = tweet.user.followers_count
        df.loc[i, 'User_location'] = tweet.user.location
        df.loc[i, 'User_verified'] = tweet.user.verified
        df.loc[i, 'rt_count'] = tweet.retweet_count
        df.loc[i, 'tweet_date'] = tweet.created_at
        
        #Enfin, je sauvegarde le résultat dans un fichier Excel en utilisant #"df.to_excel". 
        #Ici, j'utilise un espace réservé {} au lieu de nommer le fichier à l'intérieur 
        #de la fonction car je veux pouvoir le nommer moi-même lorsque j'exécute la fonction.
        df.to_excel('{}.xlsx'.format(file_name))
        i+=1
        if i == 5:
            break
        
        
        
# Maintenant, je peux simplement appeler ma fonction comme suit, 
stream(data = ['kitten'], file_name = 'kitten_list')


# Ok, maintenant je peux ouvrir la feuille Excel de mon répertoire
# pour obtenir le résultat dans mon DataFrame comme suit:
#df.head()

