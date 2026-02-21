# 🎓 EtudiantApp — TP Gestion des Étudiants (API REST)

Application client-serveur : **PHP/XAMPP** (client) ↔ **Flask/Python** (API REST).



## 📁 Structure du projet

```
TP/
├── EX1.py                        ← Serveur API Flask  ← lancer en PREMIER
│
└── Etudiant_cleint/              ← Dossier à mettre dans C:\xampp\htdocs\
    ├── test_api_.php             ← Étape 1 : Affichage brut JSON (print_r)
    ├── test_api_2.php            ← Étape 2 : Affichage HTML simple
    ├── test_api4.php             ← Étape 3 : Utilisation du service (StudentService)
    ├── test_api5.php             ← Étape 4 : Séparation Vue / Service
    ├── test_api_crud.php         ← Étape 5 : CRUD complet (liste + suppression)
    ├── config/
    │   └── config.php            ← URL de l'API Flask
    ├── services/
    │   └── StudentService.php    ← Requêtes HTTP vers l'API (cURL)
    ├── views/
    │   ├── students.php          ← Affichage de la liste
    │   ├── add_student.php       ← Formulaire ajout
    │   └── edit_student.php      ← Formulaire modification
    └── assets/
        └── style.css             ← Styles de l'interface
```

---

## 🚀 Lancement étape par étape

### 1️⃣ Installer Flask (une seule fois)

Ouvre un **cmd** et tape :
```bash
pip install flask flask-cors
```

### 2️⃣ Démarrer le serveur Flask

Dans le dossier contenant `EX1.py` :
```bash
python EX1.py
```
✅ Tu dois voir : `Running on http://127.0.0.1:5000`  
⚠️ **Laisser ce terminal ouvert pendant toute la session.**

<img width="912" height="297" alt="image" src="https://github.com/user-attachments/assets/67f5fb45-82ba-4fe0-b11c-717006cdaf12" />


### 3️⃣ Démarrer Apache dans XAMPP

- Ouvre **XAMPP Control Panel**
- Clique **Start** sur **Apache** → voyant vert ✅

### 4️⃣ Placer le dossier client

Copier `Etudiant_cleint` dans :
```
C:\xampp\htdocs\Etudiant_cleint\
```

---

## 🧪 Progression des fichiers de test

Le TP se construit **étape par étape**. Voici la progression logique :

---

### 📄 Étape 1 — `test_api_.php` — Affichage brut des données

> Appel direct à l'API Flask avec `file_get_contents()` et affichage brut avec `print_r()`.

**URL :**
```
http://localhost/Etudiant_cleint/test_api_.php
```

**Ce que tu vois dans le navigateur :**

<img width="875" height="302" alt="image" src="https://github.com/user-attachments/assets/07635f31-b236-49b7-ba86-08ac794c6f41" />


> 💡 C'est la sortie PHP brute — pas de mise en forme, juste pour vérifier que la connexion API fonctionne.

---

### 📄 Étape 2 — `test_api_2.php` — Affichage HTML simple

> On parcourt le tableau avec `foreach` et on affiche chaque étudiant en HTML basique.

**URL :**
```
http://localhost/Etudiant_cleint/test_api_2.php
```

**Ce que tu vois dans le navigateur :**

<img width="559" height="197" alt="image" src="https://github.com/user-attachments/assets/15af3995-8f4e-48c5-afeb-b9cd2dcc5f4c" />


> 💡 Premier affichage HTML — encore sans mise en forme, mais la logique de boucle est en place.

---

### 📄 Étape 3 — `test_api4.php` — Introduction du Service

> On importe `StudentService.php` pour séparer la logique d'appel HTTP du reste du code.

**URL :**
```
http://localhost/Etudiant_cleint/test_api4.php
```

**Ce que tu vois dans le navigateur :**

<img width="635" height="232" alt="image" src="https://github.com/user-attachments/assets/8bd63f08-3dea-416a-9b72-58e91c8f17c7" />


> 💡 Le résultat visuel est identique à l'étape 2, mais le code est mieux structuré : `StudentService::getAllStudents()` encapsule la requête cURL vers Flask.

---

### 📄 Étape 4 — `test_api5.php` — Séparation Vue / Service (MVC)

> On sépare complètement la vue (`views/students.php`) de la logique métier. Le fichier PHP ne fait que récupérer les données et inclure la vue.

**URL :**
```
http://localhost/Etudiant_cleint/test_api5.php
```


> 💡 La vue `students.php` génère maintenant un tableau HTML propre avec `style.css` appliqué. C'est le début de l'architecture MVC.

---

### 📄 Étape 5 — `test_api_crud.php` — Application CRUD complète ⭐

> Point d'entrée principal de l'application. Gère la liste des étudiants, la suppression, et donne accès aux formulaires d'ajout et de modification.

**URL :**
```
http://localhost/Etudiant_cleint/test_api_crud.php
```

**Ce que tu vois dans le navigateur :**

<img width="959" height="371" alt="image" src="https://github.com/user-attachments/assets/6989905b-86d2-438c-bd1c-278a74c9c820" />


**Fonctionnalités disponibles depuis cette page :**

- ✅ **Lister** tous les étudiants (appel `GET /students`)
- ✅ **Supprimer** un étudiant via le bouton 🗑️ (appel `DELETE /students/{id}`)
- ✅ **Accéder au formulaire d'ajout** → `views/add_student.php`
- ✅ **Accéder au formulaire de modification** → `views/edit_student.php`

---

### 📝 Formulaire d'ajout — `views/add_student.php`


<img width="923" height="318" alt="image" src="https://github.com/user-attachments/assets/b343a45d-f3f2-40f8-a585-abb908326a2f" />



- Envoie une requête `POST /students` vers Flask avec les données du formulaire.

---

### ✏️ Formulaire de modification — `views/edit_student.php`


<img width="937" height="398" alt="image" src="https://github.com/user-attachments/assets/474058d8-d0f7-462a-b302-e9f027165e70" />



- Pré-remplit le formulaire avec les données actuelles (appel `GET /students/{id}`).
- Envoie une requête `PUT /students/{id}` vers Flask pour la mise à jour.

---
<img width="957" height="396" alt="image" src="https://github.com/user-attachments/assets/6078b517-d993-4726-a67a-3bb3dfec2f91" />

## 🔁 Endpoints API (EX1.py)

| Action | Méthode | URL | Utilisé dans |
|--------|---------|-----|--------------|
| Lister tous | `GET` | `/students` | test_api_.php, test_api_2.php, test_api4.php, test_api5.php, test_api_crud.php |
| Voir un | `GET` | `/students/{id}` | edit_student.php |
| Ajouter | `POST` | `/students` | add_student.php |
| Modifier | `PUT` | `/students/{id}` | edit_student.php |
| Supprimer | `DELETE` | `/students/{id}` | test_api_crud.php |

---

## 🔄 Architecture globale

```
Navigateur
    │
    ▼
PHP (XAMPP :80)
    │  cURL
    ▼
Flask API (Python :5000)
    │
    ▼
Données en mémoire (liste Python)
```

---

## ❗ Problèmes fréquents

| Problème | Solution |
|----------|----------|
| Page blanche | Vérifier que Flask tourne (`python EX1.py`) |
| Erreur cURL | Activer `extension=curl` dans `C:\xampp\php\php.ini` puis redémarrer Apache |
| `file_get_contents` échoue | Utiliser cURL via `StudentService` plutôt que `file_get_contents` |
| Données perdues après restart | Normal — Flask stocke en mémoire (redémarrage = reset) |
| Port 5000 occupé | Changer le port dans `EX1.py` et mettre à jour `config/config.php` |

---

## 📚 Concepts abordés dans ce TP

- ✅ **API REST** avec Flask (Python)
- ✅ **Client HTTP** en PHP avec cURL
- ✅ **Séparation des responsabilités** : config / service / vue
- ✅ **Architecture MVC** simplifiée
- ✅ **Opérations CRUD** complètes (Create, Read, Update, Delete)
- ✅ **Communication inter-processus** via HTTP/JSON
