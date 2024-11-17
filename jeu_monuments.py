import random
import time

# Dictionnaire des monuments avec des informations détaillées
monuments = {
    "Tour Eiffel": {
        "description": "C'est une grande tour métallique située à Paris, France. Elle est un symbole mondial de la France.",
        "emplacement": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
        "année_construction": 1889,
        "architecte": "Gustave Eiffel",
        "signification_historique": "Ce monument a été construit pour l'Exposition Universelle de 1889. Elle a été le plus haut monument du monde jusqu'en 1930."
    },
    "Musée du Louvre": {
        "description": "C'est le plus grand musée d'art du monde et un monument emblématique de Paris.",
        "emplacement": "Rue de Rivoli, 75001 Paris",
        "année_construction": 1793,
        "architecte": "Pierre Lescot (initial), I. M. Pei (Pyramide)",
        "signification_historique": "Il était à l'origine un palais royal. Aujourd'hui, il abrite des œuvres célèbres telles que la Joconde et la Vénus de Milo."
    },
    "Cathédrale Notre-Dame": {
        "description": "C'est une cathédrale gothique située sur l'île de la Cité.",
        "emplacement": "6 Parvis Notre-Dame - Pl. Jean-Paul II, 75004 Paris",
        "année_construction": 1345,
        "architecte": "Maurice de Sully (initial), Jean-Baptiste-Antoine Lassus (restauration)",
        "signification_historique": "Ce monument a été un centre spirituel et culturel majeur en France, notamment pendant les événements de la Révolution française et les guerres mondiales."
    },
    "Basilique du Sacré-Cœur": {
        "description": "C'est une église située au sommet de la colline de Montmartre.",
        "emplacement": "35 Rue du Chevalier de la Barre, 75018 Paris",
        "année_construction": 1914,
        "architecte": "Paul Abadie",
        "signification_historique": "Elle est un symbole de la foi chrétienne et un lieu de pèlerinage. Elle a été construite après la défaite de la France dans la guerre franco-prussienne."
    },
    "Arc de Triomphe": {
        "description": "C'est un monument historique situé sur la place Charles de Gaulle, à l'extrémité ouest des Champs-Élysées.",
        "emplacement": "Place Charles de Gaulle, 75008 Paris",
        "année_construction": 1836,
        "architecte": "Jean Chalgrin",
        "signification_historique": "Il commémore les victoires militaires de Napoléon Bonaparte et les soldats français tombés au combat. Il abrite la tombe du Soldat Inconnu."
    }
}

# Variable globale pour le score
score = 0
temps_limite = 30  # Temps limite pour chaque question en secondes

# Fonction pour poser une question sur un monument
def poser_question(monument):
    global score
    
    bonne_reponse = monument
    autres_choix = random.sample([m for m in monuments.keys() if m != bonne_reponse], 3)
    choix = random.sample([bonne_reponse] + autres_choix, 4)

    print("\nVoici les informations sur un monument célèbre :")
    print(f"Description : {monuments[monument]['description']}")
    print(f"Emplacement : {monuments[monument]['emplacement']}")
    print(f"Année de construction : {monuments[monument]['année_construction']}")
    print(f"Architecte : {monuments[monument]['architecte']}")
    print(f"Signification historique : {monuments[monument]['signification_historique']}")
    
    print("\nQuel monument est décrit ci-dessus ?")
    for i, choix_option in enumerate(choix, 1):
        print(f"{i}. {choix_option}")
    
    # Timer pour limiter le temps de réponse
    debut_temps = time.time()
    
    try:
        reponse = int(input(f"Entrez le numéro de votre réponse (temps limite : {temps_limite} secondes) : "))
        temps_ecoule = time.time() - debut_temps
        
        if temps_ecoule > temps_limite:
            print("Temps écoulé ! Vous avez perdu des points.")
            return False
        elif choix[reponse - 1] == bonne_reponse:
            print("Bonne réponse !\n")
            score += 10
            return True
        else:
            print(f"Mauvaise réponse ! La bonne réponse était : {bonne_reponse}.\n")
            score -= 5
            return False
    except (ValueError, IndexError):
        print("Réponse invalide. Vous avez perdu des points.")
        score -= 5
        return False

# Fonction pour afficher le score actuel
def afficher_score():
    print(f"\nVotre score actuel est : {score} points")

# Boucle principale du jeu
def jouer():
    global score
    print("Bienvenue dans le jeu des monuments de Paris !\n")
    
    while True:
        monument_nom = random.choice(list(monuments.keys()))
        
        if not poser_question(monument_nom):
            print("Essayez de mieux répondre pour augmenter votre score !")
        
        afficher_score()
        
        continuer = input("\nVoulez-vous continuer à jouer ? (oui/non) : ").strip().lower()
        if continuer != "oui":
            print(f"Merci d'avoir joué ! Votre score final est : {score} points. À bientôt !")
            break

# Lancer le jeu
if __name__ == "__main__":
    jouer()
