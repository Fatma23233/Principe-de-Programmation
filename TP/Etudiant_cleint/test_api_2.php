<?php
$url = "http://localhost:5000/students";

$response = file_get_contents($url);
$students = json_decode($response, true);

echo "<h1>Liste des étudiants</h1>";
foreach ($students as $student) {
    echo $student['name'], "_", $student['age'], " ans<br>";
}
?>