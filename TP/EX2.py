from flask import Flask, jsonify, request

app = Flask(__name__)
# liste des livres
students = [
    {"id": 1, "name": "HPI", "année":2022 },
    {"id": 2, "name": "Casanova", "année": 1996},
    {"id": 3, "name": "Art de la simplicité", "année": 2018}

]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des livres !"

@app.route('/livres', methods=['GET'])
def get_livres():
    return jsonify(livres)

@app.route('/livres', methods=['POST'])
def add_livres():
    new_livre = request.get_json()
    if not new_livre.get("name") or not new_livre.get("année"):
        return jsonify({"error": "Les champs 'name' et 'année' sont requis"}), 400
    new_livre['id'] = len(livres) + 1
    students.append(new_livre)
    return jsonify(new_livre), 201

# afficher un livre sachant son identifiant

@app.route('/livres/<int:id>' , methods=['GET'])
def get_livre(id):
    livre=next((s for s in livres if s['id']==id), None)
    if livre:
        return jsonify(livre)
    return jsonify({"erreur": "'le livre n'existe pas !"}), 404


# Mettre un jour un livre PUT
@app.route('/livres/<int:id>' , methods=['PUT'])

def update_livre(id):
    livre=next((s for s in livres if s['id']==id), None)
    if not livre:
        return jsonify({"message":"Livre non trouvé !"}), 404
    
    data=request.get_json()
    student.update(data) # Mis à jour de données
    return jsonify(livre)


if __name__ == '__main__':
    app.run(debug=True)

#mimi_exo méthode DELETE