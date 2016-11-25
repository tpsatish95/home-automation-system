<?php
include_once dirname(__FILE__) . './Config.php';
function Refresh() {
        $response = array();
        $roomNum = $_POST["roomNum"];
        $db = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD,DB_NAME,3306);
        // mysql query
        $check = $db->query("SELECT * FROM room" . $roomNum);
        
        if (mysqli_num_rows($check) > 0)  {
        
        while($row = $check->fetch_assoc()) {
        $response[$row["devNum"]] = $row["status"];
        }
            
        $response["error"] = false;
        $response["message"] = "Refreshed Successfully!";    
        }
        else{
            $response["error"] = true;
            $response["message"] = "Failed to Refresh Switch Status!";
        }
       // echo json response
    echo json_encode($response);
}
Refresh();
?>