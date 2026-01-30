
# README - TP Web Service SOAP en Java

## 1️⃣ Introduction

Ce TP consiste à créer un **service Web SOAP** en Java à l’aide de **JAX-WS**. L’objectif est de comprendre :

* Qu’est-ce qu’un service Web SOAP
* Comment créer et publier un service Web en Java
* Comment tester un service Web avec son **WSDL**

À la fin, nous avons un petit service capable de :

* Convertir un montant en appliquant un coefficient (`convertir`)
* Calculer la somme de deux nombres (`somme`)

---

## 2️⃣ Prérequis

Pour réaliser ce TP, il faut avoir installé sur votre machine :

1. **Java 8** (JDK 8)
2. **IntelliJ IDEA** (ou un autre IDE Java compatible)
3. **SoapUI** pour tester le service Web

---

## 3️⃣ Technologies utilisées

| Technologie         | Description simple                                                                                                                                                                                              |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SOAP**            | Protocole pour échanger des messages entre applications via XML.                                                                                                                                                |
| **JAX-WS**          | API Java qui permet de créer des services Web SOAP facilement grâce aux annotations.                                                                                                                            |
| **JAXB**            | Permet de transformer des objets Java en XML et vice versa (sérialisation / désérialisation).                                                                                                                   |
| **URL / URI / URN** | Manières d’identifier une ressource sur le web : <br>• URL : adresse pour accéder à une ressource. <br>• URN : nom unique d’une ressource. <br>• URI : combinaison de URL et URN pour identifier une ressource. |

---

## 4️⃣ Structure du projet

Le projet contient deux classes principales :

### 4.1 `MonserviceWeb.java`

Cette classe définit notre **service Web**.

```java
@WebService(targetNamespace ="http//www.universiteParisNord.fr")
public class MonserviceWeb {
    @WebMethod(operationName = "convertir")
    public double conversion(double mt){
        return mt*0.9;
    }

    public double somme(@WebParam(name="parametre1") double a, double b){
        return a+b;
    }
}
```

**Explications simples :**

* `@WebService` : indique que cette classe est un **service Web**.
* `targetNamespace` : permet de distinguer ce service si plusieurs services ont le même nom.
* `@WebMethod` : permet de donner un **nom spécifique** à une méthode exposée.
* `@WebParam` : permet de donner un **nom lisible aux paramètres** pour le client.

La classe fournit donc deux services simples :

1. `convertir` : multiplie un montant par 0.9
2. `somme` : additionne deux nombres

---

### 4.2 `Application.java`

Cette classe publie le service pour qu’il soit accessible sur le réseau.

```java
import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.println("Début du déploiement de mon service");

        String url = "http://localhost:8888/serviceSoap";
        Endpoint.publish(url, new MonserviceWeb());

        System.out.println("Le service Web est déployé !");
    }
}
```

**Explications simples :**

* `Endpoint.publish(url, service)` : démarre le service Web à l’adresse indiquée.
* L’URL doit **toujours contenir un chemin après le port**, ici `/serviceSoap`.
* Une fois lancé, le WSDL est accessible à :

```
http://localhost:8888/serviceSoap?wsdl
```

---

## 5️⃣ Tester le service Web

Pour tester le service SOAP, on utilise **SoapUI** :

1. Installer SoapUI depuis [https://www.soapui.org/downloads/](https://www.soapui.org/downloads/)
2. Créer un **SOAP Project** et entrer le WSDL :

```
http://localhost:8888/serviceSoap?wsdl
```

3. SoapUI génère automatiquement les méthodes du service (`convertir` et `somme`).
4. On peut envoyer des requêtes et visualiser les réponses.

💡 **Important :** Le service Java (`Application.java`) doit être en cours d’exécution avant de tester avec SoapUI.

---

## 6️⃣ Résultat attendu

* Quand tu lances `Application.java`, la console affiche :

```
Début du déploiement de mon service
Le service Web est déployé !
```

* En ouvrant le navigateur sur :

```
http://localhost:8888/serviceSoap?wsdl
```

Tu vois la description XML du service (WSDL).

* Dans SoapUI, tu peux appeler :

  * `convertir(100)` → `90.0`
  * `somme(5, 7)` → `12.0`

---

## 7️⃣ Conclusion

Grâce à ce TP :

* Tu sais créer un **service Web SOAP simple en Java**
* Tu sais **annoter une classe avec JAX-WS** pour exposer des méthodes
* Tu sais **tester un service SOAP avec SoapUI**
* Tu comprends la différence entre **URL, URN et URI**
* Tu sais quels outils installer pour travailler : **Java 8, IntelliJ et SoapUI**

C’est la base pour construire des services Web plus complexes dans le futur.



