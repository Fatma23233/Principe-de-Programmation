<?php
require_once __DIR__ . '/config/config.php';
require_once __DIR__ . '/services/StudentService.php';

// Supprimer un étudiant si demandé
if (isset($_GET['delete'])) {
    StudentService::deleteStudent($_GET['delete']);
    header('Location: /Etudiant_cleint/test_api_crud.php');
    exit;
}

// Récupérer tous les étudiants
$students = StudentService::getAllStudents();

// Afficher la vue
require_once __DIR__ . '/views/students.php';