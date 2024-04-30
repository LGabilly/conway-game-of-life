# Jeu de la Vie de Conway

Ce projet implémente une simulation du célèbre [*Jeu de la Vie* de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) en Python, avec une interface basée sur Curses pour une expérience utilisateur interactive.

## Fonctionnalités

- Simulation du Jeu de la Vie de Conway.
- Interface utilisateur basée sur Curses pour une visualisation en temps réel.
- Paramètres personnalisables pour contrôler la durée de la simulation, l'échelle du motif et la densité de population initiale.

## Installation

1. Clonez ce référentiel :

```bash
git clone git@github.com:LGabilly/conway-game-of-life.git
```

2. Assurez-vous d'avoir Python installé sur votre système.

3. Installez les dépendances en exécutant :

```bash
pip install -r requirements.txt
```

## Utilisation

Vous pouvez exécuter la simulation avec les paramètres par défaut ou spécifier les paramètres personnalisés :

```bash
python -m src.main --gen 50 --scale 20 --pop 0.5
```

- `gen`: Le nombre de générations à simuler.
- `scale`: Le facteur d'échelle pour le motif.
- `pop`: La probabilité qu'une cellule soit vivante dans le motif aléatoire.

## Exemple

![Jeu de la Vie de Conway](exemple.gif)
