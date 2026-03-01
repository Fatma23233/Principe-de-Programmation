from flask import Flask, jsonify, request
from flask_cors import CORS
import repository

# Créer l'application
app = Flask(__name__)
CORS(app)  #  autorise les requêtes depuis index.html ouvert en local


# ── Route de test ────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return "C'est cool REST !"


# ── GET /students  →  liste de tous les étudiants ───────────────────────────
@app.route('/students', methods=['GET'])
def get_students():
    students = repository.get_all_students()
    return jsonify(students), 200


# ── GET /students/<id>  →  un étudiant par son id ───────────────────────────
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = repository.get_student_by_id(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


# ── POST /students  →  ajouter un étudiant ──────────────────────────────────
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')   
    age  = data.get('age')

    if not name or age is None:
        return jsonify({"error": "name et age requis"}), 400

    new_id = repository.add_student(name, age)
    return jsonify({"id": new_id, "name": name, "age": age}), 201


# ── PUT /students/<id>  →  modifier un étudiant ─────────────────────────────
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    age  = data.get('age')

    if not name or age is None:
        return jsonify({"error": "name et age requis"}), 400

    affected = repository.update_student(student_id, name, age)

    if affected == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"id": student_id, "name": name, "age": age}), 200


# ── DELETE /students/<id>  →  supprimer un étudiant ─────────────────────────
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    affected = repository.delete_student(student_id)

    if affected == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Étudiant supprimé"}), 200


# ── Lancement du serveur ─────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)