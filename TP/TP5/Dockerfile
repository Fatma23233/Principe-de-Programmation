Pour exécuter notre API dans un conteneur, nous avons créé le Dockerfile suivant :

On commence par utiliser une image Python légère :
FROM python:3.12-slim

Ensuite, on définit le dossier de travail dans le conteneur :
WORKDIR /app

On installe ensuite le framework nécessaire à l’application :
RUN pip install flask

Puis on copie l’ensemble des fichiers du projet dans le conteneur :
COPY . /app/

On précise ensuite le port utilisé par l’application :
EXPOSE 5000

Enfin, on définit la commande qui lance le serveur :
CMD ["python", "serveur_student.py"]

Lancement de l’application

Pour construire l’image Docker :
docker build -t mon-app-tp2 .

Puis pour démarrer le conteneur en reliant le port local au port du conteneur :
docker run -p 4900:5000 mon-app-tp2

Une fois le serveur lancé (visible via les logs), il est possible de tester l’API en ouvrant :
http://localhost:4900
