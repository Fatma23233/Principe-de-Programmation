

## Création du Dockerfile

Dans cette partie, nous avons conteneurisé l’API développée lors du TP2 à l’aide d’un **Dockerfile**, puis nous l’avons exécutée de manière isolée.

### Empaquetage de l’API

L’API est construite en suivant les étapes suivantes :

1. Définir le dossier de travail à l’intérieur du conteneur
2. Installer le framework **Flask**
3. Copier les fichiers du projet dans le conteneur
4. Indiquer le port utilisé par l’application
5. Définir la commande de démarrage

### Commandes de lancement

Pour construire l’image :

```bash
docker build -t mon-app-tp2 .
```

Pour lancer le conteneur (en reliant le port 4900 de la machine au port 5000 du conteneur) :

```bash
docker run -p 4900:5000 mon-app-tp2
```

### Test de l’API

Une fois le conteneur lancé, il suffit d’ouvrir un navigateur à l’adresse suivante :
[http://localhost:4900](http://localhost:4900)

⚠️ Attention : pour que l’API soit accessible depuis l’extérieur du conteneur, il est nécessaire de configurer le serveur Flask avec :

```python
app.run(host='0.0.0.0', port=5000)
```


