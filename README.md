# Createk_Omer - README

Bienvenue dans le dépôt GitHub **Createk** ! Ce projet contient deux applications interactives et ludiques : une **calculatrice web** et un jeu appelé **Chi Fou Mi** (pierre-papier-ciseaux). Voici un guide détaillé pour que tu puisses explorer, comprendre et tester chaque projet, même si tu es nouveau en informatique.

---

## Clone du dépôt

Pour commencer, tu dois cloner ce dépôt sur ton ordinateur. Ouvre un terminal et exécute cette commande :

```bash
git clone git@github.com:teddsk/Createk_Omer.git
```
Cela téléchargera tous les fichiers du projet sur ton ordinateur.

---

## 1. **Calcultor** (Calculatrice Web)

### Description
La calculatrice web est une application simple et élégante qui te permet de faire des calculs mathématiques directement dans ton navigateur. Elle est facile à utiliser et a été conçue pour être intuitive.

### Stack utilisée
- **HTML** : pour structurer la page web.
- **CSS** : pour le style et la mise en page.

### Fonctionnalités principales :
- Effectuer des opérations mathématiques de base : addition, soustraction, multiplication et division.
- Effacer les entrées avec un bouton "C".
- Résultat instantané en appuyant sur le bouton "=".

### Comment tester ?
1. Ouvre un terminal et navigue dans le dossier `Calcultor` :
   ```bash
   cd Createk_Omer/Calcultor
   ```
2. Ouvre le fichier **Calculatrice.html** dans un navigateur (par exemple, Google Chrome ou Firefox) :
   - Sous Linux : 
     ```bash
     xdg-open Calculatrice.html
     ```
   - Sous Windows : double-clique sur le fichier `Calculatrice.html`.
   - Sous macOS : 
     ```bash
     open Calculatrice.html
     ```
3. Une fois la calculatrice ouverte dans le navigateur :
   - Utilise les boutons pour entrer des chiffres et effectuer des calculs.
   - Le bouton `=` affiche le résultat.
   - Le bouton `C` efface tout.

### Astuces supplémentaires :
- L'arrière-plan est personnalisable, avec une image incluse dans le fichier CSS.
- Passe la souris sur les boutons pour voir un effet "hover" amusant !

---

## 2. **Chi Fou Mi** (Pierre-Papier-Ciseaux)

### Description
**Chi Fou Mi** est un jeu web où tu peux jouer au célèbre jeu pierre-papier-ciseaux. Cette version inclut un système de connexion pour enregistrer les joueurs.

### Stack utilisée
- **Django** : framework backend pour gérer la logique et les utilisateurs.
- **Templates Django (HTML, CSS)** : pour créer les pages web interactives.
- **SQLite3** : base de données pour enregistrer les comptes des utilisateurs.

### Fonctionnalités principales :
- S'inscrire et se connecter.
- Jouer à "Pierre-Papier-Ciseaux" contre d'autres joueurs ou l'ordinateur.

### Prérequis
Avant de commencer, tu dois installer Python et les dépendances nécessaires.
1. Assure-toi que Python est installé sur ton ordinateur.
2. Installe les dépendances avec la commande suivante (dans le dossier `chi_fou_mi`) :
   ```bash
   pip install -r requirements.txt
   ```

### Comment tester ?
1. Navigue dans le dossier `chi_fou_mi` :
   ```bash
   cd Createk_Omer/chi_fou_mi
   ```
2. Active l'environnement virtuel :
   ```bash
   source env/bin/activate
   ```
3. Lance le serveur Django :
   ```bash
   cd game
   python manage.py runserver
   ```
4. Une fois le serveur démarré, ouvre ton navigateur et accède à cette adresse :
   [http://127.0.0.1:8000/sign/](http://127.0.0.1:8000/sign/)

### Étapes pour jouer :
1. **Inscription** :
   - Remplis le formulaire d'inscription avec un nom d'utilisateur et un mot de passe.
2. **Connexion** :
   - Connecte-toi avec tes identifiants.
3. **Commence à jouer** :
   - Suis les instructions sur la page pour défier un adversaire ou l'ordinateur.

---

## Remarques
- Si tu rencontres des problèmes techniques, vérifie que toutes les dépendances sont bien installées.
- Le jeu "Chi Fou Mi" utilise une base de données SQLite pour gérer les comptes des utilisateurs.


Contact

Si tu as des questions, des suggestions ou des problèmes, tu peux contacter les membres du projet :

Omer Dedo : omer.dedo@epitech.eu

Abiola Fayemi : abiola.fayemi@epitech.eu

Katia Elegbe : katia.elegbe@epitech.eu

Ted Dossou-Koko : ted.dossou-koko@epitech.eu

Amuse-toi bien et découvre les bases du développement web avec ces projets ! Si tu as des idées d'amélioration, n'hésite pas à contribuer.

