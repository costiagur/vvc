<?php

class db {

    private $pdo;

    function connect(){
        
        try {
            $this->pdo = new PDO(
                "mysql:host=localhost;dbname=vvc;charset=utf8",
                "vvcuser",
                "password");
            
                $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                
       } catch (PDOException $e) {
            throw new PDOException($e->getMessage(), (int)$e->getCode());
       }        
        
    }

    //******************  CLOSE CONNECTION  ************************************************ */
    
    function close(){
        $this->pdo = null;
    }


    //***************** SELECT VVC DATA ***************************************************** */

    function selectuser($username){
            
        $stmt = "SELECT DISTINCT myfullname, myoffice, myorg, myphone, mymobile, myemail, mywebsite, myaddress FROM report WHERE myusername = ?";

        $runstmt = $this->pdo->prepare($stmt);

        $runstmt->execute([$username]);

        $resultarr = $runstmt->fetchAll(PDO::FETCH_ASSOC);

        return($resultarr[0]);
    }


    //***************  CLEAN  ********************************************************************/
    
    function clean($dirty){
        
        if(isset($dirty)){

            $midval = $this->pdo->quote($dirty);

            $midval = implode(array_slice(str_split($midval,1),1,-1)); //remove extra quotes
            
        }
        else{
            $midval = '""';
        }
        
        return $midval;
    }

}
?>


