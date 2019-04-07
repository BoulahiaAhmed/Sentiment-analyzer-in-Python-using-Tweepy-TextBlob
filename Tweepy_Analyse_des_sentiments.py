# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:36:28 2019

@author: MyComputer
"""

import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

#consumer Key
ckey= 'rHFGKNJkgJfXzZcZgoTLLtlBf'
#consumer Secret
csecret= '4TysL3W2MUQivu6eB5UlBBIJRQwHSb1TLjU6S8jMFCqcGLQzGq'
#access Token
atoken='1084591454230581249-X97MNBRlhKSWZ3ptQrCuBQC6kKu8ah'
# access Token Secret
asecret='2vRv2npgLcKyc7wx4IdUZ3lBEVhGuzXwKN2K7uP9eLzK5'

#PARTIE D'AUTENTIFICATION
#on crée une instance de OAuthHandler dans laquelle on passe notre consumer Key et consumer Secret
auth = tweepy.OAuthHandler(ckey, csecret)
#on équipe OAuthHandler avec nos access Token
auth.set_access_token(atoken, asecret)
#avec cette commande on va avoir accès a tous les methodes du class API, et on va avoir un accée directe au data du Twitter
api =tweepy.API(auth)

#fonction pour calculer le pourcentage
def percentage(part,whole):
    return 100 * float(part)/float(whole)


# input pour  mot-clé / tag a cherché avec le nombre de tweets.
Mot_cle = input("Entrez un mot-clé / un tag pour faire une recherche: ")
Nbr_Mot_cle = int(input("Entrez le nombre de tweets à rechercher: "))

#PARCOUR DES TWEETS
#pour avoir les tweets d'un seul timeline on utilise les commandes suivants:
#api.user_timeline(id="twitter")
#tweepy.Cursor(api.user_timeline, id="twitter")
#version='extended'
#.full_text
#et pour ajouter une limitation a notre recherche on ajoute .tems() , et si on veut une limitation par nombre de pages on met .pages() 
tweets=tweepy.Cursor(api.search, q=Mot_cle, lang='en').items(Nbr_Mot_cle)

#On initialise le nombre des sentiments a 0
positive = 0
negative = 0
neutre = 0
#la somme des setiments 
polarity = 0

#On prcour les tweets importé du twitter et on fait notre analyse de sentiments avec la methode TextBlob
for tweet in tweets: 
    analysis = TextBlob(tweet.text)
    print(tweet.text)
    print(analysis.sentiment.polarity)
    
    print('* * * * *      * * * * * * * * *        * * * * * * * * * * *      * * * * * ')
    
    
    #Classification des sentiments
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity==0):
        neutre +=1

    elif (analysis.sentiment.polarity<0.0):
        negative +=1

    elif (analysis.sentiment.polarity>0.0):
        positive +=1

#calcul de pourcentage
positive = percentage(positive, Nbr_Mot_cle )        
neutre = percentage(neutre, Nbr_Mot_cle ) 
negative = percentage(negative, Nbr_Mot_cle ) 
polarity = percentage(polarity, Nbr_Mot_cle ) 

# modification du format a un float avec deux chiffres apres virgule

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutre, '.2f')

#print resultat
print ("Comment les gens réagissent sur " + Mot_cle + " en analysant " + str (Nbr_Mot_cle) + " Tweets.")

if (polarity ==0):
    print("neutre")
elif(polarity < 0):
    print("Negative")
elif(polarity > 0):
    print("Positive")
    
#Ici on a choisit pie chart pour representer graphiquement nos données

labels =['positive ['+str(positive)+'%]' , 'neutre ['+str(neutral)+'%]' , 'negative ['+str(negative)+'%]' ]
sizes = [positive,neutral,negative]
colors =['green' ,'yellow','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("Comment les gens réagissent sur" + Mot_cle + " en analysant " + str (Nbr_Mot_cle)  + "Tweets.")
plt.axis('equal')
plt.tight_layout()

plt.show()






























