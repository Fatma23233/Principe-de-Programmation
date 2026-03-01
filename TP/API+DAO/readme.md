# 🎓 StudentAPI — TP Gestion des Étudiants (API REST + Dashboard)

Application **API REST** Python/Flask avec base de données **MySQL** et dashboard **HTML/JS** intégré.

---

## 📁 Structure du projet

```
TP/
├── app.py            ← Serveur API Flask          ← lancer en PREMIER
├── repository.py     ← Couche DAO (requêtes SQL)
├── db.py             ← Connexion MySQL
├── config.py         ← Paramètres de connexion BDD
├── schema.sql        ← Script de création de la BDD  ← exécuter une seule fois
└── index.html        ← Dashboard client (ouvrir dans le navigateur)
```

---

## 🚀 Lancement étape par étape

### 1️⃣ Installer les dépendances (une seule fois)

Ouvre un **cmd** et tape :
```bash
pip install flask flask-cors mysql-connector-python
```

### 2️⃣ Démarrer MySQL dans XAMPP

- Ouvre **XAMPP Control Panel**
- Clique **Start** sur **MySQL** → voyant vert ✅

### 3️⃣ Créer la base de données (une seule fois)

```bash
mysql -u root < schema.sql
```

Cela crée la base `school_api` avec la table `students` et 3 étudiants de test (Alice, Bob, Charlie).

 <img width="943" height="461" alt="image" src="https://github.com/user-attachments/assets/ae52071d-a306-4796-b736-04f3e6a5485d" />


### 4️⃣ Démarrer le serveur Flask

Dans le dossier du projet :
```bash
python app.py
```
✅ Tu dois voir : `Running on http://0.0.0.0:5001`  

<img width="474" height="172" alt="image" src="https://github.com/user-attachments/assets/ccbf183e-018c-4d38-8cbb-14b7073665f6" />

⚠️ **Laisser ce terminal ouvert pendant toute la session.**

### 5️⃣ Ouvrir le dashboard

Ouvre `index.html` dans ton navigateur.  
Le dashboard se connecte automatiquement à `http://127.0.0.1:5001` et affiche les étudiants.


<img width="747" height="329" alt="image" src="https://github.com/user-attachments/assets/2c49a2ff-b5b1-4e79-a880-0adf54ba3448" />

---

## 🖥️ Le Dashboard (`index.html`)

<img width="753" height="460" alt="image" src="https://github.com/user-attachments/assets/63e5f825-2986-46e0-857e-0bcd0607c868" />


Interface web complète qui consomme l'API directement depuis le navigateur via `fetch()`.

**Fonctionnalités disponibles :**

- ✅ **Lister** tous les étudiants (appel `GET /students`)
- ✅ **Ajouter** un étudiant via le formulaire (appel `POST /students`)
- ✅ **Modifier** un étudiant via le bouton ✏️ (appel `PUT /students/{id}`)
- ✅ **Supprimer** un étudiant via le bouton 🗑️ (appel `DELETE /students/{id}`)
- ✅ **Statut API** en temps réel (connecté / hors ligne)
- ✅ **Compteur** d'étudiants et dernière opération effectuée

---

## 🔁 Endpoints API (`app.py`)

| Action | Méthode | URL | Corps JSON |
|--------|---------|-----|------------|
| Lister tous | `GET` | `/students` | — |
| Voir un | `GET` | `/students/{id}` | — |
| Ajouter | `POST` | `/students` | `{ "name": "Alice", "age": 20 }` |
| Modifier | `PUT` | `/students/{id}` | `{ "name": "Alice", "age": 21 }` |
| Supprimer | `DELETE` | `/students/{id}` | — |

### Exemples curl

```bash
# Lister tous les étudiants
curl http://127.0.0.1:5001/students

# Voir un étudiant
curl http://127.0.0.1:5001/students/1

# Ajouter un étudiant
curl -X POST http://127.0.0.1:5001/students \
     -H "Content-Type: application/json" \
     -d '{"name": "Diana", "age": 21}'

# Modifier un étudiant
curl -X PUT http://127.0.0.1:5001/students/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "age": 22}'

# Supprimer un étudiant
curl -X DELETE http://127.0.0.1:5001/students/1
```

---

## 🗄️ Base de données (`schema.sql`)

```sql
CREATE DATABASE IF NOT EXISTS school_api CHARACTER SET utf8mb4;

CREATE TABLE students (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    age        INT NOT NULL CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔄 Architecture globale

```
Navigateur
    │
    ▼
index.html (HTML + JS fetch)
    │  HTTP/JSON (port 5001)
    ▼
Flask API — app.py  (Python :5001)
    │  appel Python
    ▼
repository.py  (DAO — requêtes SQL)
    │  mysql-connector
    ▼
MySQL / XAMPP  (port 3306)
    │
    ▼
Base de données : school_api › table students
```

---

## 🧱 Rôle de chaque fichier

| Fichier | Rôle |
|---------|------|
| `app.py` | Définit les routes Flask et gère les requêtes/réponses HTTP |
| `repository.py` | Couche DAO — toutes les requêtes SQL (SELECT, INSERT, UPDATE, DELETE) |
| `db.py` | Crée et retourne une connexion MySQL |
| `config.py` | Centralise les paramètres de connexion (host, port, user, password, database) |
| `schema.sql` | Script SQL pour créer la BDD et insérer des données de test |
| `index.html` | Dashboard client — UI complète en HTML/CSS/JS vanilla |

---

## ❗ Problèmes fréquents

| Problème | Solution |
|----------|----------|
| Dashboard "Hors ligne" | Vérifier que Flask tourne (`python app.py`) |
| Erreur connexion MySQL | Vérifier que MySQL est démarré dans XAMPP |
| `ModuleNotFoundError: flask_cors` | Lancer `pip install flask-cors` |
| `ModuleNotFoundError: mysql.connector` | Lancer `pip install mysql-connector-python` |
| Port 5001 déjà utilisé | Changer le port dans `app.py` (ligne `app.run(port=5001)`) |
| Données perdues | Normal si `schema.sql` a été réexécuté — cela recrée la table |

---

## 📚 Concepts abordés dans ce TP

- ✅ **API REST** avec Flask (Python)
- ✅ **Patron DAO** (Data Access Object) — séparation SQL / logique métier
- ✅ **CRUD complet** via HTTP (GET, POST, PUT, DELETE)
- ✅ **Base de données relationnelle** MySQL avec `mysql-connector-python`
- ✅ **Client JS vanilla** — `fetch()`, gestion async/await, manipulation du DOM
- ✅ **CORS** — communication cross-origin entre `index.html` et Flask
- ✅ **Architecture en couches** : Route → Repository → DB
