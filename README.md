# Projet météo en Python

Application en ligne de commande qui affiche la météo actuelle d'une ville saisie par l'utilisateur.

Projet réalisé dans le cadre du TP guidé *Utiliser GitHub pour gérer et suivre un projet informatique* (Culture numérique 3, EPF).

**Auteur :** ROZEN--THOMAS Titouan (2A)

## Contexte

Ce projet sert de support pour apprendre à utiliser Git et GitHub : dépôt distant, commits réguliers, historique lisible et documentation. Le programme lui-même est volontairement simple afin que le travail porte surtout sur la gestion de versions.

## Objectifs

- Mettre en pratique le cycle Git/GitHub : `clone`, `add`, `commit`, `push`.
- Réaliser plusieurs commits significatifs répartis sur les étapes du développement.
- Documenter le projet (README, `requirements.txt`).
- Obtenir un programme fonctionnel à la date de remise.

## Fonctionnalités

- Recherche des coordonnées GPS d'une ville à partir de son nom.
- Récupération de la météo actuelle : conditions, température, température ressentie, humidité, pluie et vent.
- Traduction en français des codes météo (ciel dégagé, brouillard, pluie, neige, orage...).
- Affichage lisible dans le terminal.
- Gestion des erreurs :
  - ville introuvable ou saisie vide : la ville est redemandée ;
  - `q` pour quitter le programme ;
  - absence de connexion internet, serveur trop lent ou autre erreur réseau : message d'erreur clair, sans plantage.

## Technologies utilisées

| Élément | Rôle |
|---|---|
| Python 3 | Langage du programme |
| [requests](https://requests.readthedocs.io/) | Requêtes HTTP vers les API |
| [API Open-Meteo](https://open-meteo.com/) (géocodage et prévisions) | Coordonnées des villes et données météo (aucune clé d'API nécessaire) |
| Git et GitHub | Gestion de versions et hébergement du dépôt |

## Structure du projet

```
projet_meteo_python/
├── src/
│   └── main.py          # programme principal
├── .gitignore
├── README.md
└── requirements.txt     # dépendances Python
```

## Installation et exécution

Prérequis : Python 3 et Git installés.

```bash
git clone https://github.com/TopStriker001/projet_meteo_python.git
cd projet_meteo_python
pip install -r requirements.txt
python src/main.py
```

Le programme demande alors une ville :

```
Ville (q pour quitter) :
```

### Exemple d'affichage

Les valeurs ci-dessous sont indicatives.

```
==================================
  Météo à Paris
==================================
  Conditions  : Partiellement nuageux
  Température : 12.3 °C
  Ressenti    : 10.8 °C
  Humidité    : 76 %
  Pluie       : 0.0 mm
  Vent        : 14.5 km/h
==================================
```

## Historique du développement

| N° | Hash | Étape |
|---|---|---|
| 1 | `af78f9f` | Création de la structure du projet |
| 2 | `96a4d87` | Base du programme et `requirements.txt` |
| 3 | `5e3cb1f` | Recherche des coordonnées GPS d'une ville |
| 4 | `003dedd` | Récupération des données météo actuelles |
| 5 | `de4f5ef` | Affichage propre et lisible dans le terminal |
| 6 | `62f811e` | Gestion des villes inconnues et des erreurs de saisie ou réseau |
| 7 | `e49541f` | Ajout de la pluie, de l'humidité, du ressenti et des conditions |

## Source des données

Données météo et de géocodage fournies par [Open-Meteo](https://open-meteo.com/).