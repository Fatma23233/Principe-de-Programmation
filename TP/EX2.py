from flask import Flask, jsonify, request

app = Flask(__name__)

# Liste des livres
livres = [
    {"id": 1, "name": "HPI", "année": 2022},
    {"id": 2, "name": "Casanova", "année": 1996},
    {"id": 3, "name": "Art de la simplicité", "année": 2018}
]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des livres !"

# GET : Tous les livres
@app.route('/livres', methods=['GET'])
def get_livres():
    return jsonify(livres)

# POST : Ajouter un livre
@app.route('/livres', methods=['POST'])
def add_livre():
    new_livre = request.get_json()
    if not new_livre.get("name") or not new_livre.get("année"):
        return jsonify({"error": "Les champs 'name' et 'année' sont requis"}), 400
    new_livre['id'] = max([l['id'] for l in livres]) + 1 if livres else 1
    livres.append(new_livre)
    return jsonify(new_livre), 201

# GET : Livre par id
@app.route('/livres/<int:id>', methods=['GET'])
def get_livre(id):
    livre = next((l for l in livres if l['id'] == id), None)
    if livre:
        return jsonify(livre)
    return jsonify({"erreur": "Le livre n'existe pas !"}), 404

# PUT : Mettre à jour un livre
@app.route('/livres/<int:id>', methods=['PUT'])
def update_livre(id):
    livre = next((l for l in livres if l['id'] == id), None)
    if not livre:
        return jsonify({"message": "Livre non trouvé !"}), 404
    
    data = request.get_json()
    livre.update(data)
    return jsonify(livre)

# DELETE : Supprimer un livre
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    livre = next((l for l in livres if l['id'] == id), None)
    if not livre:
        return jsonify({"message": "Livre non trouvé !"}), 404
    livres.remove(livre)
    return jsonify({"message": f"Le livre {id} a été supprimé."})

if __name__ == '__main__':
    app.run(debug=True)
