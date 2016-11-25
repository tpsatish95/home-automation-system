<?php
include_once dirname(__FILE__) . './Config.php';
function getstatus() {
        $response = array();
        $roomNum = (string)$_GET["roomNum"];
        $devNum = (string)$_GET["devNum"];

        $db = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD,DB_NAME,3306);
        // mysql query
        $result = "";
        // mysql query
        $result = $db->query("SELECT * FROM room" . $roomNum . " where devNum ='$devNum'");    
        
        while($row = $result->fetch_assoc()) {
        $response["status"] = $row["status"];
        }

        if ($result) {
            $response["error"] = false;
            $response["message"] = "DB status successfully retrieved!";
        } else {
            $response["error"] = true;
            $response["message"] = "DB connection failed!";
        }
       // echo json response
    echo json_encode($response);
}
getstatus();
?>