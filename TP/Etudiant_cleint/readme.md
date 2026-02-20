# 🎓 EtudiantApp — TP Gestion des Étudiants (API REST)

Application client-serveur : **PHP/XAMPP** (client) ↔ **Flask/Python** (API REST).

---

## 📁 Structure du projet

```
TP/
├── EX1.py                        ← Serveur API Flask  ← lancer en PREMIER
│
└── Etudiant_cleint/              ← Dossier à mettre dans C:\xampp\htdocs\
    ├── test_api_crud.php         ← Point d'entrée (liste + suppression)
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

Vérifie : ouvre [http://127.0.0.1:5000/students](http://127.0.0.1:5000/students) → tu dois voir du JSON.

### 3️⃣ Démarrer Apache dans XAMPP

- Ouvre **XAMPP Control Panel**
- Clique **Start** sur **Apache** → voyant vert ✅

### 4️⃣ Placer le dossier client

Copier `Etudiant_cleint` dans :
```
C:\xampp\htdocs\Etudiant_cleint\
```

### 5️⃣ Ouvrir l'application

```
http://localhost/Etudiant_cleint/test_api_crud.php
```

---

## 🔁 Endpoints API (EX1.py)

| Action | Méthode | URL |
|--------|---------|-----|
| Lister | `GET` | `/students` |
| Voir un | `GET` | `/students/{id}` |
| Ajouter | `POST` | `/students` |
| Modifier | `PUT` | `/students/{id}` |
| Supprimer | `DELETE` | `/students/{id}` |

---

## ❗ Problèmes fréquents

| Problème | Solution |
|----------|----------|
| Page blanche | Vérifier que Flask tourne (`python EX1.py`) |
| Erreur cURL | Activer `extension=curl` dans `C:\xampp\php\php.ini` puis redémarrer Apache |
| Données perdues | Normal, Flask stocke en mémoire (redémarrage = reset) |
