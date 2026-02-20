<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des étudiants</title>
    <link rel="stylesheet" href="/Etudiant_cleint/assets/style.css">
</head>
<body>

<!-- Header -->
<header class="site-header">
    <a class="brand" href="/Etudiant_cleint/test_api_crud.php">🎓 EtudiantApp</a>
    <span class="api-tag">TP — API REST</span>
</header>

<div class="container">

    <h1 class="page-title">Liste des étudiants</h1>
    <p class="page-subtitle">Gestion des étudiants via l'API Flask</p>

    <!-- Barre d'outils -->
    <div class="toolbar">
        <div class="count-badge">
            <span><?= count($students) ?></span> étudiant<?= count($students) > 1 ? 's' : '' ?>
        </div>
        <a href="/Etudiant_cleint/views/add_student.php" class="btn btn-primary">
            ＋ Ajouter un étudiant
        </a>
    </div>

    <!-- Tableau -->
    <div class="card">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nom</th>
                    <th>Âge</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
            <?php if (empty($students)): ?>
                <tr>
                    <td colspan="4">
                        <div class="empty">
                            <div class="empty-icon">🎓</div>
                            <p>Aucun étudiant. Commencez par en ajouter un !</p>
                        </div>
                    </td>
                </tr>
            <?php else: ?>
                <?php foreach ($students as $student) : ?>
                <tr>
                    <td><span class="id-chip">#<?= htmlspecialchars($student['id']) ?></span></td>
                    <td><span class="name-cell"><?= htmlspecialchars($student['name']) ?></span></td>
                    <td><span class="age-chip"><?= htmlspecialchars($student['age']) ?> ans</span></td>
                    <td>
                        <div class="actions-cell">
                            <a href="/Etudiant_cleint/views/edit_student.php?id=<?= $student['id'] ?>"
                               class="btn btn-edit">✏️ Modifier</a>
                            <a href="/Etudiant_cleint/test_api_crud.php?delete=<?= $student['id'] ?>"
                               class="btn btn-delete"
                               onclick="return confirm('Supprimer <?= htmlspecialchars($student['name']) ?> ?')">
                               🗑️ Supprimer
                            </a>
                        </div>
                    </td>
                </tr>
                <?php endforeach; ?>
            <?php endif; ?>
            </tbody>
        </table>
    </div>

</div>
</body>
</html>
