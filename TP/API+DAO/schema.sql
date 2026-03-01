-- Créer la base
CREATE DATABASE IF NOT EXISTS school_api CHARACTER SET utf8mb4;
USE school_api;

-- Créer la table students
CREATE TABLE IF NOT EXISTS students (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,   
    age        INT NOT NULL CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Données de test
INSERT INTO students (name, age) VALUES
    ('Alice',   20),
    ('Bob',     22),
    ('Charlie', 19);