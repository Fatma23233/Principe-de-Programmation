
# TP7 : Architecture multi-services avec Docker Compose

Ce TP présente la mise en place d’une architecture composée de plusieurs services (microservices) à l’aide de **Docker Compose**.
Contrairement à une gestion manuelle des conteneurs, Docker Compose permet d’orchestrer l’ensemble de l’infrastructure à partir d’un seul fichier de configuration.

---

## 1. Intérêt de Docker Compose

Docker Compose permet de simplifier le déploiement d’applications composées de plusieurs services (ex : base de données, API, frontend, cache, etc.).

Ses principaux avantages sont :

* Décrire toute l’architecture dans un seul fichier : `docker-compose.yml`
* Démarrer tous les services avec une seule commande : `docker compose up`
* Gérer automatiquement le réseau entre les conteneurs
* Faciliter la reproductibilité et le partage de l’environnement

---

## 2. Architecture du projet

Le projet est organisé en plusieurs services :

```text
TP7_PP/
│
├── docker-compose.yml     # Orchestrateur global
│
├── product/               # Service backend (API Python)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── api.py
│
└── website/               # Service frontend (PHP)
    └── index.php
```

---

## 3. Description des services

### 3.1 Backend (service API) : `/product`

Ce service contient la logique métier de l’application, développée en Python avec Flask.

* `api.py` : API REST qui retourne une liste de produits au format JSON
* `requirements.txt` : liste des dépendances (Flask, Flask-RESTful)
* `Dockerfile` : définit l’environnement d’exécution (installation des dépendances et lancement du serveur)

---

### 3.2 Frontend (service web) : `/website`

Ce service représente l’interface utilisateur.

* `index.php` : page web qui consomme l’API backend
* Communication interne : le frontend appelle l’API via le nom du service Docker

Exemple :

```php
file_get_contents('http://product-service/');
```

Grâce à Docker Compose, le nom du service devient une adresse réseau interne, ce qui évite de gérer des IPs manuellement.

---

### 3.3 Orchestration : `docker-compose.yml`

Ce fichier définit et connecte tous les services.

Il gère :

* **Build et images** : construction de l’API et utilisation d’une image PHP Apache
* **Ports** : exposition des services vers la machine hôte (5001 et 5002)
* **Volumes** : synchronisation entre le code local et les conteneurs
* **Dépendances** : démarrage du backend avant le frontend (`depends_on`)

---

## 4. Lancement du projet

### Démarrer les services

À la racine du projet :

```bash id="p7c1xq"
docker compose up
```

Pour exécuter en arrière-plan :

```bash id="k2v9aa"
docker compose up -d
```

---

### Tester l’application

Accéder au frontend via :
[http://localhost:5002](http://localhost:5002)

---

## 5. Gestion de l’exécution

Lors de l’exécution, plusieurs options sont disponibles :

* `d` : détacher l’exécution (mode background)
* `v` : ouvrir Docker Desktop
* `w` : activer le mode watch (rechargement automatique)
* `o` : afficher la configuration Docker interprétée

---

## 6. Arrêter l’application

Pour arrêter tous les services :

```bash id="q8m1tt"
docker compose down
```

---

## 7. Remarque importante (cache Docker)

Si des modifications sont apportées à des fichiers comme `requirements.txt`, Docker peut réutiliser une ancienne image en cache.

Dans ce cas, il faut forcer la reconstruction :

```bash id="x4l9zz"
docker compose up --build
```


