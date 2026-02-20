<?php
require_once __DIR__ . '/config/config.php';
require_once __DIR__ . '/services/StudentService.php';

// Récupérer les étudiants via le service
$students = StudentService::getAllStudents();

// Afficher la vue
require_once __DIR__ . '/views/students.php';