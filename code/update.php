<?php
include_once dirname(__FILE__) . './Config.php';
function update() {
        $response = array();
        $roomNum = $_GET["roomNum"];
        $devNum = $_GET["devNum"];
        $status = $_GET["status"];
        $db = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD,DB_NAME,3306);
        // mysql query
        $result = "";
       // mysql query
        $result = $result = $db->query("UPDATE room" . $roomNum . " set status = $status where devNum ='$devNum'");
        
        if ($result) {
            $response["error"] = false;
            $response["message"] = "Switch Status Changed Successfully !";
        } else {
            $response["error"] = true;
            $response["message"] = "Failed to Change Switch Status!";
        }
       // echo json response
    echo json_encode($response);
}
update();
?>