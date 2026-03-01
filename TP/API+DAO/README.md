# API REST – Flask + MySQL

Architecture **API + DAO** en Python.

## Structure

```
API+DAO/
├── app.py          # Couche API (routes Flask)
├── repository.py   # Couche DAO (requêtes SQL)
├── db.py           # Connexion MySQL
├── config.py       # Paramètres de connexion
└── schema.sql      # Script de création de la BDD
```

## Installation

```bash
pip3 install flask mysql-connector-python
```

## Configuration

Modifier `config.py` selon votre environnement :

```python
DB_CONFIG = {
    "host":     "localhost",
    "port":     8889,   # 8889 (MAMP) ou 3306 (MySQL standard)
    "user":     "root",
    "password": "root",
    "database": "school_api"
}
```

## Base de données

```bash
mysql -u root -p < schema.sql
```

## Lancement

```bash
python3 app.py
```

## Endpoints

| Méthode | URL                  | Description                  | Code |
|---------|----------------------|------------------------------|------|
| GET     | `/`                  | Route de test                | 200  |
| GET     | `/students`          | Liste tous les étudiants     | 200  |
| GET     | `/students/<id>`     | Étudiant par id              | 200 / 404 |
| POST    | `/students`          | Créer un étudiant            | 201  |
| DELETE  | `/students/<id>`     | Supprimer un étudiant        | 200 / 404 |

## Exemples curl

```bash
# Lister tous les étudiants
curl http://127.0.0.1:5001/students

# Récupérer l'étudiant id=1
curl http://127.0.0.1:5001/students/1

# Créer un étudiant
curl -X POST http://127.0.0.1:5001/students \
     -H "Content-Type: application/json" \
     -d '{"prenom": "Diana", "age": 21}'

# Supprimer l'étudiant id=1
curl -X DELETE http://127.0.0.1:5001/students/1
```
