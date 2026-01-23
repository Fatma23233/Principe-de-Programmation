from flask import Flask , jsonify , request
# creer l'application Flask
app=Flask(__name__)
# Une liste d'etudiants
students =[
    {"id":1, "name": "Youcef", "age":21},
    {"id":2, "name": "Samir", "age":41}
]
# Racine de l'API pour tester si le serveur fonctionne ......
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des etudiants !"
# Activer mode Debug pour voir les erreurs et recharger automatiquement le serverur
if __name__=='__main__':
    app.run(debug=True)
