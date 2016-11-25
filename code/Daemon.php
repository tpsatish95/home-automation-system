<?php
include_once dirname(__FILE__) . './Config.php';
function postInstance() {
        $response = array();
        $roomNum = $_POST["roomNum"];
        $devNum = $_POST["devNum"];
        $status = $_POST["status"];
        $result = "";
        $db = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD,DB_NAME,3306);
        // mysql query
        $check = $db->query("SELECT * FROM room" . $roomNum . " where devNum ='$devNum'");
        $query = "INSERT INTO room" . $roomNum . "(devNum,status) VALUES('$devNum',$status)";
        $update = "UPDATE room" . $roomNum . " set status = $status where devNum ='$devNum'";
        if (mysqli_num_rows($check) > 0)  {
        
        $result = $db->query($update);    
            
        }
        else{
        
        $result = $db->query($query);
            
        }
        if ($result) {
            $response["error"] = false;
            $response["message"] = "Switch Status Changed Successfully successfully!";
        } else {
            $response["error"] = true;
            $response["message"] = "Failed to Change Switch Status!";
        }
       // echo json response
    echo json_encode($response);
}
postInstance();
?>