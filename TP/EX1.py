from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
    {"id": 3, "name": "Fatima", "age": 22}

]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    if not new_student.get("name") or not new_student.get("age"):
        return jsonify({"error": "Les champs 'name' et 'age' sont requis"}), 400
    new_student['id'] = len(students) + 1
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
