<?php

class StudentService
{
    public static function getAllStudents()
    {
        $url = API_BASE_URL . '/students';
        $response = file_get_contents($url);
        return json_decode($response, true);
    }

    public static function getStudent($id)
    {
        $url = API_BASE_URL . '/students/' . $id;
        $response = file_get_contents($url);
        return json_decode($response, true);
    }

    public static function addStudent($data)
    {
        $url = API_BASE_URL . '/students';
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        $response = curl_exec($ch);
        curl_close($ch);
        return json_decode($response, true);
    }

    public static function updateStudent($id, $data)
    {
        $url = API_BASE_URL . '/students/' . $id;
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        $response = curl_exec($ch);
        curl_close($ch);
        return json_decode($response, true);
    }

    public static function deleteStudent($id)
    {
        $url = API_BASE_URL . '/students/' . $id;
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);
        return $response;
    }
}
