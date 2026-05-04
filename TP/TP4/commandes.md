

# Suivi des commandes utilisées pendant le TP Docker

Ce document regroupe les différentes commandes utilisées au cours du TP.

## Tests de base

On commence par vérifier que Docker fonctionne correctement :

* Lancement d’une image de test : `docker run hello-world`
* Test en mode interactif : `docker run -it alpine:latest /bin/sh`

Ensuite, on construit notre propre image avec la commande :
`docker build -t mon-alpine-custom .`

Cette commande signifie :

* `docker build` : créer une image à partir d’un fichier **Dockerfile**
* `-t mon-alpine-custom` : donner un nom (tag) à l’image
* `.` : utiliser le dossier courant comme contexte

Une fois l’image créée, on vérifie qu’elle fonctionne en lançant un conteneur :
`docker run -it mon-alpine-custom`

On peut aussi tester la connexion internet depuis le conteneur avec :
`curl http://google.com`

## Nginx, ports et bind mounts

On met ensuite en place un serveur web et on lie un fichier local au conteneur.

On crée une page `index.html`, puis on lance un serveur Nginx avec :
`docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name monServeurWeb nginx`

Cette commande permet de :

* lancer le conteneur en arrière-plan
* exposer le port 80 du conteneur sur le port 8080 de la machine
* partager le dossier courant avec le conteneur (bind mount)

On peut ensuite accéder au site via :
[http://localhost:8080](http://localhost:8080)

## Réseaux et volumes gérés (Named Volumes)

Pour organiser les conteneurs et gérer le stockage de manière propre, on crée :

* Un réseau :
  `docker network create monreseau-prive`

* Un volume Docker :
  `docker volume create ma-bdd-data`

Puis on lance un serveur MySQL avec :
`docker run -d --name base-de-donnees --network monreseau-prive -v ma-bdd-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:8.0`

En résumé, cette commande :

* lance le conteneur en arrière-plan (`-d`)
* lui donne le nom *base-de-donnees*
* le connecte au réseau privé créé
* associe un volume pour stocker les données de façon persistante
* définit le mot de passe root nécessaire au démarrage de MySQL
* utilise l’image officielle MySQL version 8.0


