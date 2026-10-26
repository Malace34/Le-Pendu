# Jeu du pendu

Un jeu du pendu en Python, à jouer dans le terminal. L'ordinateur choisit un mot au hasard, et le joueur doit le deviner lettre par lettre avant que le dessin du pendu ne soit complet.

## Fonctionnalités

- Mot choisi au hasard dans une liste
- Affichage du mot masqué (`_ _ _ _`) qui se dévoile au fil des bonnes lettres
- 6 vies, avec un dessin du pendu en ASCII qui évolue à chaque erreur
- Affichage des lettres déjà proposées
- Vérification des saisies (une seule lettre, pas de lettre répétée)
- Possibilité de rejouer à la fin d'une partie

## Lancer le jeu

Il faut avoir [Python 3](https://www.python.org/downloads/) installé.

1. Téléchargez le fichier `pendu.py` (ou clonez le dépôt).
2. Ouvrez un terminal dans le dossier du fichier.
3. Lancez :

   python pendu.py

Vous pouvez aussi ouvrir le fichier dans Thonny et cliquer sur « Run ».

## Comment jouer

1. Le mot à trouver apparaît sous forme de tirets.
2. Proposez une lettre à chaque tour.
3. Si la lettre est dans le mot, elle est révélée. Sinon, vous perdez une vie et le pendu se dessine un peu plus.
4. Vous gagnez si vous trouvez toutes les lettres, vous perdez si vous n'avez plus de vies.

## Ce que j'ai appris

- Les chaînes de caractères et les listes
- Les fonctions avec paramètres et valeur de retour
- Les boucles `while` et `for`, avec `continue`
- La validation des saisies utilisateur

#
