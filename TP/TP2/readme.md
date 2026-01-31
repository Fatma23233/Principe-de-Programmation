
# README – TP2 : Web Service SOAP avec objets (Etudiant)

## 1️⃣ Objectif du TP2

Ce TP2 est la **suite directe du TP1**.
Dans le TP1, nous avons créé un service Web SOAP qui échangeait des **types simples** (double).

**Dans le TP2**, l’objectif est d’aller plus loin en :

* Manipulant des **objets Java**
* Envoyant un **objet `Etudiant` via SOAP**
* Comprenant le rôle de **JAXB** pour la sérialisation XML

---

## 2️⃣ Lien avec le TP1

| TP1                                              | TP2                                         |
| ------------------------------------------------ | ------------------------------------------- |
| Méthodes retournant des types simples (`double`) | Méthodes retournant des objets (`Etudiant`) |
| `conversion`, `somme`                            | `conversion`, `somme`, **`getEtudiant`**    |
| SOAP + JAX-WS                                    | SOAP + JAX-WS + JAXB                        |

Le TP2 **réutilise le même service**, mais l’enrichit avec une nouvelle méthode.

---

## 3️⃣ Prérequis

Pour réaliser ce TP, il faut avoir installé :

* **Java 8 (JDK 8)**
* **IntelliJ IDEA**
* **SoapUI**

⚠️ Le service doit être **en cours d’exécution** pour pouvoir être testé.

---

## 4️⃣ Technologies utilisées

| Technologie | Rôle                                         |
| ----------- | -------------------------------------------- |
| **SOAP**    | Protocole d’échange de messages basé sur XML |
| **JAX-WS**  | Création de services Web SOAP en Java        |
| **JAXB**    | Conversion objet Java ⇄ XML                  |
| **WSDL**    | Description du service Web                   |
| **SoapUI**  | Outil de test des services SOAP              |

---

## 5️⃣ Description du service Web

### 5.1 Classe `MonserviceWeb`

```java
@WebService(targetNamespace ="http//www.universiteParisNord.fr")
public class MonserviceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt){
        return mt * 0.9;
    }

    public double somme(@WebParam(name="parametre1") double a, double b){
        return a + b;
    }

    public Etudiant getEtudiant(int identifiant){
        return new Etudiant(1, "Thom", 19);
    }
}
```

### Explication simple :

* `conversion` : retourne un nombre réel
* `somme` : additionne deux nombres
* **`getEtudiant`** : retourne un **objet Java** de type `Etudiant`

 Cette méthode montre que SOAP peut **envoyer des objets complexes**, pas seulement des nombres.

---

## 6️⃣ Classe `Etudiant`

```java
@XmlRootElement
public class Etudiant implements Serializable {

    private int identifiant;
    private String nom;
    private double moyenne;

    public Etudiant() {
        // constructeur sans paramètres obligatoire pour JAXB
    }

    public Etudiant(int identifiant, String nom, double moyenne) {
        this.identifiant = identifiant;
        this.nom = nom;
        this.moyenne = moyenne;
    }

    // getters et setters
}
```

### Explications :

* `@XmlRootElement` : permet à JAXB de transformer l’objet en XML
* `Serializable` : autorise l’envoi de l’objet
* Le **constructeur sans paramètres est obligatoire** pour SOAP/JAXB

Sans ces éléments, l’objet ne peut pas être envoyé correctement.

---

## 7️⃣ Vérification via le navigateur (WSDL)

Après le lancement de l’application, on accède au WSDL à l’adresse :

```
http://localhost:8888/serviceSoap?wsdl
```

### 🔎 Résultat attendu :

* Le WSDL affiche maintenant **3 méthodes** :

  * `convertir`
  * `somme`
  * **`getEtudiant`**

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/ffd493b3-8701-42ac-bdd5-0025dc813796" />


> *WSDL affichant la méthode getEtudiant*

---

## 8️⃣ Test avec SoapUI

### Étapes :

1. Ouvrir SoapUI
2. Mettre à jour le projet (**Update Definition**)
3. SoapUI recharge le WSDL
4. La méthode **`getEtudiant` apparaît automatiquement**

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/527338cc-d6f0-4518-94a6-dc0f4a510cd4" />


> *SoapUI montrant getEtudiant dans la liste des requêtes*

## 9️⃣ Schéma de fonctionnement (TP1 + TP2)

```
Client SoapUI
      |
      |  Requête SOAP
      v
Service Web (MonserviceWeb)
      |
      |  Objet Etudiant
      v
Conversion JAXB (Java ⇄ XML)
```

---

## 🔟 Conclusion

Grâce à ce TP2, nous avons appris à :

* Étendre un service Web SOAP existant (TP1)
* Envoyer des **objets Java** via SOAP
* Utiliser **JAXB** pour la sérialisation XML
* Vérifier les méthodes via le **WSDL**
* Tester les objets retournés avec **SoapUI**

Le TP2 montre une utilisation plus réaliste des services Web SOAP, proche des applications réelles.


