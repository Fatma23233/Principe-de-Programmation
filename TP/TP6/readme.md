
# TP6 : Publication sur Docker Hub

Ce TP porte sur la publication et le partage d’images Docker via **Docker Hub**.

## 1. Création d’une image basique (Alpine)

Dans un premier temps, nous utilisons une image très légère basée sur **Alpine Linux** afin d’afficher un simple message.

L’objectif est de suivre le cycle complet de création et de publication d’une image Docker.

### Étapes de création et publication

1. Construire l’image localement :

```bash
docker build -t mon-app .
```

2. Tester l’image en local :

```bash
docker run mon-app
```

Résultat attendu : *“Bonjour à toi”*

3. Se connecter à Docker Hub :

```bash
docker login
```

4. Ajouter un tag à l’image (en utilisant le nom d’utilisateur Docker Hub) :

```bash
docker tag mon-app mathurasanthalingam/mon-app:1
```

5. Publier l’image sur Docker Hub :

```bash
docker push mathurasanthalingam/mon-app:1
```

---

## 2. Utilisation de l’image publiée

Une fois publiée, l’image peut être utilisée depuis n’importe quelle machine avec la commande :

```bash
docker run username/mon-app:1
```

---

## 3. Remarque importante (compatibilité)

Dans certains cas, une erreur de type **manifest incompatible** peut apparaître si l’image a été construite sur une architecture différente (ex : Windows vs Mac).

Pour résoudre ce problème, il est possible de forcer l’émulation de plateforme :

```bash
docker run --platform linux/amd64 username/mon-app:1
```


