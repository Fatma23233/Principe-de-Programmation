<?php
// Inclure la configuration et le service
require_once __DIR__ . '/config/config.php';
require_once __DIR__ . '/services/StudentService.php';

// Récupérer tous les étudiants via le service
$students = StudentService::getAllStudents();

// Affichage
echo "<h1>Liste des étudiants</h1>";

if ($students) {
    foreach ($students as $student) {
        echo $student['name'], "_", $student['age'], " ans<br>";
    }
} else {
    echo "Impossible de récupérer les données.";
}