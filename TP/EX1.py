# ------------------------------------------------------------
# Description générale :
# Cette application est une API REST simple développée avec Flask.
# Elle permet de gérer une liste d'étudiants en mémoire (CRUD).
# L'API expose plusieurs endpoints accessibles via HTTP afin de :
# - consulter la liste des étudiants
# - ajouter un étudiant
# - consulter un étudiant par son identifiant
# - mettre à jour les informations d'un étudiant
#
# Objectifs pédagogiques :
# - Comprendre le fonctionnement d'une API REST
# - Manipuler les méthodes HTTP (GET, POST, PUT)
# - Illustrer l'architecture client-serveur via HTTP
# - Mettre en pratique la communication backend avec JSON
# - Faire le lien avec les notions de microservices et REST vues en cours
# ------------------------------------------------------------


from flask import Flask, jsonify, request

app = Flask(__name__)
# ------------------------------------------------------------
# Données simulées (base de données en mémoire)
# Chaque étudiant est représenté par un dictionnaire Python
# ------------------------------------------------------------

students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
    {"id": 3, "name": "Fatima", "age": 22}

]
# ------------------------------------------------------------
# Endpoint racine
# Méthode : GET
# Objectif : vérifier que l'API fonctionne
# ------------------------------------------------------------
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"
# ------------------------------------------------------------
# Endpoint : récupérer la liste de tous les étudiants
# Méthode : GET
# URL : /students
# Retour : liste des étudiants au format JSON
# ------------------------------------------------------------

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)
# ------------------------------------------------------------
# Endpoint : ajouter un nouvel étudiant
# Méthode : POST
# URL : /students
# Données attendues : name et age (format JSON)
# ------------------------------------------------------------

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    if not new_student.get("name") or not new_student.get("age"):
        return jsonify({"error": "Les champs 'name' et 'age' sont requis"}), 400
    new_student['id'] = len(students) + 1
    students.append(new_student)
    return jsonify(new_student), 201
  # ------------------------------------------------------------
# Endpoint : afficher un étudiant par son identifiant
# Méthode : GET
# URL : /students/<id>
# ------------------------------------------------------------  

# afficher un etudiant sachant son identifiant

@app.route('/students/<int:id>' , methods=['GET'])
def get_student(id):
    student=next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur": "'l'etudiant n'existe pas !"}), 404
# ------------------------------------------------------------
# Endpoint : mettre à jour un étudiant
# Méthode : PUT
# URL : /students/<id>
# Objectif : modifier les informations d'un étudiant existant
# ------------------------------------------------------------

# Mettre un jour un etudiant PUT
@app.route('/students/<int:id>' , methods=['PUT'])

def update_student(id):
    student=next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify({"message":"Etudiant non trouvé !"}), 404
    
    data=request.get_json()
    student.update(data) # Mis à jour de données
    return jsonify(student)
# ------------------------------------------------------------
# Lancement de l'application Flask
# L'API est accessible par défaut sur :
# http://localhost:5000
# ------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

#mimi_exo méthode DELETE
