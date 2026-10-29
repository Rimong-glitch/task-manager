# Task Manager (CLI)

Petit gestionnaire de tâches en ligne de commande, écrit en Python.
Projet du module Gestion de Projets (TP B) — ING 3A GL, Université Ferhat Abbas Sétif 1.

## Description
Permet d'ajouter, lister, terminer et supprimer des tâches. Les tâches sont sauvegardées dans un fichier JSON.

## Structure
```
├── README.md
├── src/
│   └── main.py      # point d'entrée + décomposition (Task, TaskStorage, TaskManager, CLI)
└── tests/
    └── test_main.py # tests unitaires (unittest)
```

## Utilisation
```bash
python src/main.py add "Écrire le rapport"
python src/main.py list
python src/main.py done 1
python src/main.py delete 1
```

## Tests
```bash
python -m unittest discover -s tests
```

## Décomposition du projet
1. `Task` : modèle (id, titre, statut)
2. `TaskStorage` : lecture/écriture JSON
3. `TaskManager` : logique métier (add, list, done, delete)
4. `main()` : interface en ligne de commande (argparse)

## Auteur
AbdelRahim — ING 3A GL
