# 🌟 Principe de Programmation – Cours & Travaux Pratiques

## 📌 Présentation générale

Bienvenue dans ce dépôt GitHub !  
Il regroupe **tout le contenu du cours** ainsi que **les TP réalisés** dans le cadre du module **Principe de Programmation**.

* Ce n'est pas un projet unique, mais un **ensemble pédagogique**.
* Chaque TP met en pratique les notions **théoriques du cours**.
* L'objectif : comprendre **comment les applications modernes communiquent et sont distribuées**.

---

## 🎯 Objectifs pédagogiques globaux

Ce dépôt te permet de :

* Comprendre les **architectures distribuées**
* Explorer les **services web SOAP et REST**
* Mettre en pratique la **programmation orientée objet et l'échange de données**
* Relier la **théorie à la pratique** à travers des TP concrets
* Se familiariser avec les outils modernes (Java, Python, Flask, Docker, SOAP UI, Git)

---

## 🧠 Contenu du cours (Théorie)

Le cours couvre les concepts suivants :

* **Framework vs Bibliothèque** – structure imposée vs boîte à outils appelée par le développeur
* **Microservices et interopérabilité**
* **Architectures distribuées et monolithiques**
* **Architecture maître–esclave**
* **RMI (Remote Method Invocation)** – invocation de méthodes distantes en Java
* **CORBA** – évolution multi-langages de RMI, plus complexe
* **Services Web SOAP & REST**
* **API et communication client–serveur via HTTP**
* **Scalabilité horizontale et verticale**
* **Conteneurisation avec Docker** – images, conteneurs, Dockerfile, volumes, réseaux, Docker Compose
* **ORM (Object Relational Mapping)** – pont entre objets Python/Java et bases de données relationnelles
* **Kubernetes** – orchestration de conteneurs à grande échelle (suite logique de Docker Compose)

> Chaque notion est accompagnée de **schémas, exemples et comparatifs** pour faciliter la compréhension.

---

## 🧪 Travaux Pratiques (TP)

### 🔹 TP0 – Introduction aux Services Web (Python)

**Technologies utilisées :** Python, Flask, Requests

**Objectifs du TP :**

* Comprendre la communication **client–serveur** de base
* Créer un **serveur Flask** et un **client Python** qui interagissent
* Résoudre une **énigme** via un échange client–serveur

**Composants :**

* `serveur_student.py` + `client_student.py` → API étudiants avec client dédié
* `serveur_enigme.py` + `client_enigme.py` → échange client–serveur autour d'une énigme

> Ce TP pose les bases de la communication réseau avant d'aborder les vrais services web.

---

### 🔹 TP1 – Service Web SOAP (Java)

**Technologies utilisées :** Java 8, JAX-WS, JAXB, IntelliJ IDEA, SOAP UI

**Objectifs du TP :**

* Créer un **service SOAP** exposant des méthodes simples
* Sérialiser un **objet Java (`Etudiant`)** en XML via JAXB
* Publier le service et consulter le **WSDL**
* Tester avec **SOAP UI**

**Fonctions principales :**

* `conversion(double mt)` → conversion de montant
* `somme(double a, double b)` → somme de deux nombres
* `getEtudiant(int id)` → retourne un objet `Etudiant` sérialisé en XML

> Ce TP illustre l'interopérabilité, la communication client–serveur et la manipulation d'objets distribués.

---

### 🔹 TP2 – Client PHP ↔ API REST Python

**Technologies utilisées :** Python, Flask, PHP, XAMPP, cURL, JSON, HTTP

**Objectifs du TP :**

* Consommer une **API REST Flask** depuis un **client PHP**
* Structurer progressivement un projet en séparant **config / service / vue**
* Appliquer une architecture **MVC** simplifiée

**Progression des exercices :**

* `exo1–3` → Connexion à l'API, affichage brut puis HTML, boucle `foreach`
* `exo4` → Centralisation de la configuration (`config/config.php`)
* `exo5` → Introduction d'un **Service** (`StudentService.php`)
* `exo6` → Séparation de la **Vue** (`views/students.php`)
* `exo7` → Finalisation avec HTML5 & CSS3

> Ce TP montre comment un client PHP et une API Python Flask communiquent via HTTP/JSON, et introduit les bonnes pratiques d'architecture.

---

### 🔹 TP3 – API REST avec DAO et base de données (Python)

**Technologies utilisées :** Python, Flask, SQLite, Docker

**Objectifs du TP :**

* Créer une **API REST** connectée à une vraie **base de données**
* Implémenter le pattern **DAO (Data Access Object)**
* Conteneuriser l'ensemble avec un **Dockerfile**
* Tester les opérations CRUD avec un **script de test automatisé**

**Composants :**

* `app.py` → routes Flask
* `repository.py` → couche d'accès aux données (DAO)
* `db.py` / `config.py` → connexion et configuration BDD
* `base.sql` → schéma de la base
* `test.py` → tests automatisés (add / update / delete)

> Ce TP introduit la persistance réelle des données et le découpage en couches (API → DAO → BDD).

---

### 🔹 TP4 – Introduction à Docker

**Technologies utilisées :** Docker, Alpine, Nginx

**Objectifs du TP :**

* Créer et manipuler des **images et conteneurs** Docker
* Rédiger un **Dockerfile** basique
* Comprendre le **mapping de ports** et les volumes
* Maîtriser les commandes essentielles Docker

**Concepts mis en pratique :**

* `docker build / run / exec / stop / rm` → cycle de vie d'un conteneur
* `-v` → montage de volumes pour la persistance
* `-p` → mapping de ports
* Images légères basées sur **Alpine**

> Ce TP pose les bases de la conteneurisation avant d'aborder des architectures multi-services.

---

### 🔹 TP5 – Conteneurisation d'une API Flask

**Technologies utilisées :** Docker, Python, Flask

**Objectifs du TP :**

* Conteneuriser l'API développée en TP2 dans un **Dockerfile**
* Configurer Flask pour être accessible depuis l'extérieur du conteneur (`host='0.0.0.0'`)
* Mapper les ports entre la machine hôte et le conteneur

**Commandes clés :**

```bash
docker build -t mon-app-tp2 .
docker run -p 4900:5000 mon-app-tp2
```

> Ce TP illustre la portabilité d'une application : une fois conteneurisée, elle tourne identiquement sur n'importe quelle machine.

---

### 🔹 TP6 – Publication sur Docker Hub

**Technologies utilisées :** Docker, Docker Hub, Alpine

**Objectifs du TP :**

* Publier une image Docker sur **Docker Hub**
* Comprendre le cycle complet : build → tag → push → pull
* Gérer les problèmes de **compatibilité d'architecture** (Windows vs Mac)

**Étapes :**

1. `docker build -t mon-app .`
2. `docker run mon-app` → vérification locale
3. `docker login`
4. `docker tag mon-app username/mon-app:1`
5. `docker push username/mon-app:1`

> Une fois publiée, l'image est accessible depuis n'importe quelle machine dans le monde avec un simple `docker run`.

---

### 🔹 TP7 – Architecture multi-services avec Docker Compose

**Technologies utilisées :** Docker Compose, Python, Flask, PHP, Apache

**Objectifs du TP :**

* Orchestrer plusieurs services avec **Docker Compose**
* Faire communiquer un **backend Python** et un **frontend PHP** via un réseau interne
* Comprendre les notions de build, volumes, ports et dépendances dans un `docker-compose.yml`

**Architecture :**

```text
TP7/
├── docker-compose.yml       ← Chef d'orchestre
├── product/                 ← Backend API (Python/Flask)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── api.py
└── website/                 ← Frontend (PHP/Apache)
    └── index.php
```

**Commandes :**

```bash
docker compose up           # Démarrer tous les services
docker compose up --build   # Forcer la reconstruction des images
docker compose down         # Tout arrêter
```

> Ce TP illustre concrètement les microservices : chaque service est indépendant, isolé, et ils communiquent entre eux via le réseau interne Docker.

---

## 🔗 Lien cours ↔ TP

| Notion théorique         | TP correspondant                              |
| ------------------------ | --------------------------------------------- |
| Client–Serveur basique   | TP0 (Python client/serveur)                   |
| Interopérabilité         | SOAP (TP1) / REST (TP2, TP3)                  |
| Services Web             | Java SOAP (TP1) / Python Flask (TP2, TP3)     |
| Objet distribué          | `Etudiant` sérialisé XML / JSON               |
| DAO & persistance BDD    | TP3 (API + SQLite + DAO)                      |
| Client-Serveur HTTP      | Navigateur / SOAP UI / API REST / PHP cURL    |
| Scalabilité              | Microservices indépendants (TP7)              |
| Conteneurisation Docker  | Dockerfile (TP4, TP5) / Docker Hub (TP6)      |
| Docker Compose           | Architecture multi-services (TP7)             |
| CORBA                    | Théorique uniquement (pas de TP)              |
| Kubernetes               | Théorique uniquement (pas de TP)              |

---

## 🛠️ Prérequis techniques

Pour exécuter et tester les TP :

* **Java 8** + **IntelliJ IDEA**
* **Python 3** + **Flask** (`pip install flask flask-cors`)
* **PHP** + **XAMPP** (pour les TP PHP)
* **Docker** + **Docker Compose**
* **SOAP UI** (TP1)
* Navigateur Web
* **Git** pour cloner le dépôt

---

## ✅ Conclusion

Ce dépôt est une **ressource complète** combinant :

* Théorie 
* Pratique 
* Illustration visuelle 

Il permet de comprendre **les fondamentaux des architectures distribuées et des services web** tout en se familiarisant avec les outils et méthodes utilisés dans le développement moderne.

*Explore, expérimente, et amuse-toi en programmant !*

---

💡 **Astuce :** Suis la progression dans l'ordre : TP (bases réseau) → TP1 (SOAP) → TP2 (REST + PHP) → TP3 (DAO + BDD) → TP4/5/6 (Docker) → TP7 (Docker Compose). Chaque TP s'appuie sur le précédent !
