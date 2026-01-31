
# Cours – Architectures distribuées, interopérabilité et services Web

Ce cours présente les **concepts essentiels** pour construire, comprendre et maintenir des **applications modernes, modulaires et distribuées**.
Il s’appuie sur des **exemples concrets réalisés en TP (TP1 & TP2)** basés sur **SOAP, JAX-WS et Java**.

Nous aborderons :

* Les microservices et l’interopérabilité
* Les architectures distribuées
* L’architecture maître-esclave
* Remote Method Invocation (RMI)
* Les services Web SOAP et REST

Chaque section contient **des définitions, des explications, des schémas et un lien avec les TPs**.

---

## 1. Définitions et notions clés

### 1.1 Microservices

Un **microservice** est une application **autonome**, spécialisée dans une **fonction précise**, communiquant avec d’autres services via des **API**.

**Avantages :**

* Développement indépendant
* Déploiement séparé
* Scalabilité ciblée
* Maintenance facilitée

> **Exemple réel (TP1 & TP2)**
> Le service SOAP développé agit comme un microservice exposant :
>
> * `conversion`
> * `somme`
> * `getEtudiant`

![Image](https://microservices.io/i/Microservice_Architecture.png)

![Image](https://miro.medium.com/0%2AxuHRipbS0io0EYVl.png)

---

### 1.2 API (Application Programming Interface)

Une **API** est un **contrat** qui permet à des applications différentes de communiquer.

**Types principaux :**

* **REST** → JSON / HTTP
* **SOAP** → XML / standard formel
* **GraphQL** → données ciblées

📌 **Lien TP**
Dans les TP, le service SOAP expose une **API SOAP**, décrite par un **WSDL**.

---

### 1.3 Interopérabilité

👉 **Interopérabilité** = capacité de systèmes différents à communiquer **sans dépendre du langage ou de la plateforme**.

**Assurée par :**

* Standards (SOAP, REST)
* Formats universels (XML, JSON)
* Description formelle (WSDL)

📌 **TP1 / TP2**
SoapUI (client) ↔ Service Java
➡️ deux outils différents, mais communication réussie grâce à SOAP.

---

### 1.4 Architecture monolithique vs distribuée

* **Monolithique** : une seule application, tout est couplé
* **Distribuée** : services indépendants

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/1%2AaSdnOJNT2UoiaAhy-vuV_Q.png)

![Image](https://www.clariontech.com/hubfs/Monolithic%20Architecture%20Vs.%20Microservices.jpg)

📌 **TP**
Ton service SOAP est **un premier pas vers une architecture distribuée**.

---

### 1.5 Scalabilité

* **Verticale** : augmenter les ressources d’un serveur
* **Horizontale** : multiplier les services

📌 Les microservices (et services SOAP) facilitent la scalabilité horizontale.

---

### 1.6 Architecture maître-esclave

* Le **maître** coordonne
* Les **esclaves** exécutent
* Tolérance aux pannes

![Image](https://www.researchgate.net/publication/324673919/figure/fig3/AS%3A617699520565248%401524282450069/A-graphical-illustration-of-the-modified-master-slave-architecture-with-which-we.png)

![Image](https://www.researchgate.net/publication/317299391/figure/fig1/AS%3A540208529670144%401505807158195/Master-slave-architecture.png)

---

### 1.7 RMI – Remote Method Invocation

RMI permet d’appeler une méthode sur un **objet distant Java**.

**Cycle :**

1. Client → stub
2. Sérialisation
3. Exécution distante
4. Désérialisation

![Image](https://www.edm2.com/images/9/92/Rmi.gif)

![Image](https://infolab.stanford.edu/CHAIMS/Doc/Details/Protocols/rmi/rmi1.gif)

📌 **Comparaison TP**

* RMI : Java uniquement
* SOAP : multi-langage → **plus universel**

---

## 2. De l’interopérabilité aux microservices

### 2.1 Pourquoi l’interopérabilité est essentielle

Sans interopérabilité :

* impossible de connecter des systèmes hétérogènes
* dépendance forte à une technologie

Avec SOAP / REST :

* indépendance
* évolutivité
* ouverture

![Image](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/66d5ef0de8b7d59b71cc74b7_66d5e3421948796f8bbec1f4_6%2520-%25202.09-min.jpeg)

![Image](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/media/communication-in-microservice-architecture/sync-vs-async-patterns-across-microservices.png)

---

### 2.2 Évolution vers les architectures distribuées

* Les applications grossissent
* Le monolithique devient fragile
* Les microservices permettent la modularité

📌 **Lien TP**
Ton service SOAP = **un module indépendant**.

---

### 2.3 Pourquoi adopter les microservices

* Déploiement indépendant
* Résilience
* Scalabilité
* Adaptation aux équipes agiles

![Image](https://dz2cdn1.dzone.com/storage/temp/17670225-1715269657634.png)

![Image](https://cdn.sayonetech.com/media/media/2024/09/02/sept_02_sayone_inner_2.jpg)

---

## 3. RMI et objets distribués

RMI fut une première solution pour distribuer des objets, mais :

* dépendance Java
* faible interopérabilité

SOAP et REST ont pris le relais.

📌 **Transition pédagogique**
TP1/TP2 montrent **l’évolution naturelle : RMI → SOAP**.

---

## 4. Services Web SOAP et REST

### 4.1 SOAP vs REST

| SOAP       | REST                    |
| ---------- | ----------------------- |
| XML formel | JSON léger              |
| WSDL       | Pas toujours de contrat |
| Sécurisé   | Rapide                  |

---

### 4.2 Architecture SOAP

![Image](https://www.researchgate.net/publication/220144364/figure/fig3/AS%3A667632667729923%401536187440188/SOAP-based-Web-services-architecture.png)

![Image](https://help.genesys.com/pureconnect/mergedprojects/wh_soap/desktop/img/image003.jpg)

**Composants :**

* Provider (Service Java)
* Requester (SoapUI)
* Registry (WSDL)

📌 **TP1 & TP2**

* `Application.java` → Provider
* `SoapUI` → Requester
* `?wsdl` → Registry

---

### 4.3 SOAP et objets (TP2)

Dans le TP2 :

* SOAP ne renvoie plus un simple `double`
* Il renvoie un **objet `Etudiant`**

➡️ JAXB transforme l’objet Java en XML.

📌 **Exemple réel**
`getEtudiant()` retourne :

```xml
<Etudiant>
  <identifiant>1</identifiant>
  <nom>Thom</nom>
  <moyenne>19</moyenne>
</Etudiant>
```

---

## 5. Synthèse générale (Cours + TP)

* Interopérabilité = fondation des systèmes modernes
* SOAP et REST = solutions universelles
* RMI = approche historique
* Microservices = modularité et résilience
* TP1 : échanges simples
* TP2 : échanges d’objets

👉 **Les TP illustrent concrètement la théorie du cours.**

---

### 🎯 Conclusion pédagogique

Ce cours + TP montrent le passage :

> **Théorie → Pratique → Architecture réelle**

Tu peux clairement le présenter comme :

> *“Une introduction complète aux architectures distribuées avec application pratique via SOAP et Java.”*

---

Si tu veux, je peux maintenant :

* t’aider à **insérer les vraies captures d’écran** dans le bon ordre
* transformer tout ça en **PDF universitaire**
* rédiger une **conclusion globale cours + TP**

Dis-moi 💪
