<?php

class logfile
{

    static function logreg($loggeddata, $description='',$type = ''){
        
        $existarr = [];

        $logarr[] = '<?xml version="1.0" encoding="UTF-8"?>'.PHP_EOL;
        $logarr[] = "<log>".PHP_EOL;

        $address = "log/logfile.xml";

        if(file_exists($address) == TRUE){

            $filearr = file($address); //read file as array
            $existarr = array_slice($filearr,2); //removes first 2 elements of the array

        }
        else{
            $existarr[] = "</log>";
        }

        $logarr[] = "<entry>".PHP_EOL;

        if($type !=''){

            $logarr[] = "<type>$type</type>".PHP_EOL;
        }

        $logarr[] = "<when>".date(DATE_ATOM, time())."</when>".PHP_EOL;

        $logarr[] = "<description>$description</description>".PHP_EOL;
        
        $logarr[] = "<data>$loggeddata</data>".PHP_EOL;

        $logarr[] = "</entry>".PHP_EOL;

        $total = array_merge($logarr,$existarr);


        $logfile = fopen($address, "w");

        fwrite($logfile,implode($total));

        fclose($logfile);
    }
}


?>