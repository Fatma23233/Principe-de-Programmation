
Dockerfile du TP

Pour simplifier et automatiser le travail réalisé pendant le TP, j’ai choisi de regrouper les différentes étapes dans un Dockerfile.

On commence par utiliser l’image officielle Alpine comme base :
FROM alpine:latest

Ensuite, on installe l’outil curl directement lors de la construction de l’image :
RUN apk add --no-cache curl

Enfin, on définit une commande par défaut pour lancer automatiquement un terminal lors du démarrage du conteneur :
CMD ["/bin/sh"]

Cela permet d’éviter de devoir saisir cette commande manuellement à chaque exécution.
