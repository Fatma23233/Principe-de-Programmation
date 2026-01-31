
# 🌟 Principe de Programmation – Cours & Travaux Pratiques

![banner](https://user-images.githubusercontent.com/107123456/placeholder-banner.png)
*Illustration conceptuelle des microservices et API*

---

## 📌 Présentation générale

Bienvenue dans ce dépôt GitHub ! 🎉
Il regroupe **tout le contenu du cours** ainsi que **les TP réalisés** dans le cadre du module **Principe de Programmation**.

* Ce n’est pas un projet unique, mais un **ensemble pédagogique**.
* Chaque TP met en pratique les notions **théoriques du cours**.
* L’objectif : comprendre **comment les applications modernes communiquent et sont distribuées**.

---

## 🎯 Objectifs pédagogiques globaux

Ce dépôt te permet de :

* Comprendre les **architectures distribuées** 
* Explorer les **services web SOAP et REST** 🌐
* Mettre en pratique la **programmation orientée objet et l’échange de données** 🔄
* Relier la **théorie à la pratique** à travers des TP concrets 💻
* Se familiariser avec les outils modernes (Java, Python, Flask, SOAP UI, Git) 🛠️

---

## 🧠 Contenu du cours (Théorie)

Le cours couvre les concepts suivants :

* **Microservices et interopérabilité** 
* **Architectures distribuées et monolithiques** 
* **Architecture maître–esclave** 
* **RMI (Remote Method Invocation)** 
* **Services Web SOAP & REST** 
* **API et communication client–serveur via HTTP** 
* **Scalabilité horizontale et verticale** 

> Chaque notion est accompagnée de **schémas, exemples et comparatifs** pour faciliter la compréhension.

![archi](https://user-images.githubusercontent.com/107123456/placeholder-archi.png)
*Exemple de schéma : architecture distribuée et microservices*

---

## 🧪 Travaux Pratiques (TP)

### 🔹 TP1 – Service Web SOAP (Java)

![soap](https://user-images.githubusercontent.com/107123456/placeholder-soap.png)

**Technologies utilisées :** Java 8, JAX-WS, JAXB, IntelliJ IDEA, SOAP UI

**Objectifs du TP :**

* Créer un **service SOAP** exposant des méthodes simples
* Sérialiser un **objet Java (`Etudiant`)** en XML
* Publier le service et consulter le **WSDL**
* Tester avec **SOAP UI**

**Fonctions principales :**

* `conversion(double mt)` → conversion de montant 
* `somme(double a, double b)` → somme de deux nombres 
* `getEtudiant(int id)` → retourne un objet `Etudiant` 

> Ce TP illustre l’interopérabilité, la communication client–serveur et la manipulation d’objets distribués.

---

### 🔹 TP2 – API REST (Flask / Python)

![flask](https://user-images.githubusercontent.com/107123456/placeholder-flask.png)

**Technologies utilisées :** Python, Flask, JSON, HTTP

**Objectifs du TP :**

* Créer une **API REST** avec des endpoints CRUD
* Échanger des données en **JSON**
* Tester les routes via navigateur ou outils comme Postman/Insomnia

**Endpoints principaux :**

* `GET /students` → liste des étudiants 
* `GET /students/<id>` → un étudiant particulier 
* `POST /students` → ajouter un étudiant 
* `PUT /students/<id>` → mettre à jour un étudiant 

> Ce TP montre la différence entre **REST** et **SOAP**, et illustre l’architecture client–serveur moderne.

---

## 🔗 Lien cours ↔ TP

| Notion théorique | TP correspondant                    |
| ---------------- | ------------------------------------|
| Interopérabilité | SOAP (TP1) / REST (TP2)             |
| Services Web     | Java SOAP / Python Flask            |
| Objet distribué  | `Etudiant` sérialisé XML / JSON     |
| Client-Serveur   | Navigateur / SOAP UI / API REST     |
| Scalabilité      | Microservices indépendants          |

---

## 🛠️ Prérequis techniques

Pour exécuter et tester les TP :

* **Java 8** + **IntelliJ IDEA**
* **Python 3** + **Flask**
* **SOAP UI** (TP SOAP)
* Navigateur Web
* **Git** pour cloner le dépôt

---

## ✅ Conclusion

Ce dépôt est une **ressource complète** combinant :

* Théorie 
* Pratique 
* Illustration visuelle 

Il permet de comprendre **les fondamentaux des architectures distribuées et des services web** tout en se familiarisant avec les outils et méthodes utilisés dans le développement moderne.

![fun](https://user-images.githubusercontent.com/107123456/placeholder-fun.png)
*Explore, expérimente, et amuse-toi en programmant ! *

---

💡 **Astuce :** Pour tester les TP, commence par le TP1 (SOAP), puis passe au TP2 (REST) pour comparer les technologies et observer la différence d’approche.


