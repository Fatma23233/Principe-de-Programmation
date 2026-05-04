"""
API Flask de gestion des étudiants
-----------------------------------
Ce fichier implémente une API REST simple permettant de gérer une liste d'étudiants.
"""

from flask import Flask, jsonify, request

# Création de l'application Flask
app = Flask(__name__)

# Base de données simulée (stockage en mémoire)
students = [
    {"id": 1, "name": "Mathura", "age": 25},
    {"id": 2, "name": "Emna", "age": 23},
]

# -------------------------------
# Route de test (racine de l'API)
# -------------------------------
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"


# --------------------------------------
# GET : récupérer tous les étudiants
# --------------------------------------
@app.route('/students', methods=['GET'])
def get_students():
    # jsonify convertit la liste en JSON
    return jsonify(students)


# --------------------------------------
# POST : ajouter un étudiant
# --------------------------------------
@app.route('/students', methods=['POST'])
def add_student():
    # Récupération des données envoyées par le client
    new_student = request.get_json()

    # Attribution d'un id automatique
    new_student['id'] = len(students) + 1

    # Ajout dans la liste
    students.append(new_student)

    # Retour de l'étudiant créé + code 201 (Created)
    return jsonify(new_student), 201


# --------------------------------------
# GET : récupérer un étudiant par ID
# --------------------------------------
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    # Recherche de l'étudiant par id
    student = next((s for s in students if s['id'] == id), None)

    if student:
        return jsonify(student)

    return jsonify({"erreur": "l'étudiant n'existe pas !"}), 404


# --------------------------------------
# PUT : mettre à jour un étudiant
# --------------------------------------
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)

    if not student:
        return jsonify({"message": "Etudiant non trouvé !"}), 404

    # Données envoyées par le client
    data = request.get_json()

    # Mise à jour des champs
    student.update(data)

    return jsonify(student)


# --------------------------------------
# DELETE : supprimer un étudiant
# --------------------------------------
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = next((s for s in students if s['id'] == id), None)

    if not student:
        return jsonify({"message": "Etudiant non trouvé !"}), 404

    # Suppression de la liste
    students.remove(student)

    return jsonify(student)


# --------------------------------------
# Lancement du serveur
# --------------------------------------
if __name__ == '__main__':
    # host=0.0.0.0 permet l'accès depuis Docker / extérieur
    # debug=True active le mode développement
    app.run(host="0.0.0.0", port=5000, debug=True)
