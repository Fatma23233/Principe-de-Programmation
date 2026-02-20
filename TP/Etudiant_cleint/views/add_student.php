<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../services/StudentService.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = [
        'name' => $_POST['name'],
        'age' => (int)$_POST['age']
    ];
    StudentService::addStudent($data);
    header('Location: /Etudiant_cleint/test_api_crud.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajouter un étudiant</title>
    <link rel="stylesheet" href="/Etudiant_cleint/assets/style.css">
</head>
<body>

<!-- Header -->
<header class="site-header">
    <a class="brand" href="/Etudiant_cleint/test_api_crud.php">🎓 EtudiantApp</a>
    <span class="api-tag">TP — API REST</span>
</header>

<div class="container">

    <!-- Fil d'ariane -->
    <div class="breadcrumb">
        <a href="/Etudiant_cleint/test_api_crud.php">🏠 Accueil</a>
        <span>›</span>
        <span>Ajouter un étudiant</span>
    </div>

    <!-- Formulaire -->
    <div class="form-card">
        <div class="form-card-head">➕ Nouvel étudiant</div>
        <div class="form-card-body">
            <form method="POST" action="">

                <div class="form-group">
                    <label for="name">Nom complet</label>
                    <input type="text" id="name" name="name"
                           placeholder="ex : Youcef Benali" required>
                </div>

                <div class="form-group">
                    <label for="age">Âge</label>
                    <input type="number" id="age" name="age"
                           placeholder="ex : 21" min="1" max="120" required>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-success">✅ Ajouter</button>
                    <a href="/Etudiant_cleint/test_api_crud.php" class="btn btn-back">Annuler</a>
                </div>

            </form>
        </div>
    </div>

</div>
</body>
</html>
