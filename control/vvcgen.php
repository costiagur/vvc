<?php

require "../model/db.php";
include_once "logfile.php";

$dbcon = new db();
$dbcon->connect();

$username = $_POST["q"];
$cleanusername = $dbcon->clean(strtolower($username));

$resarr = $dbcon->selectuser($cleanusername);

$vcarr = [];

$vcarr[] = "BEGIN:VCARD";
$vcarr[] = "VERSION:3.0";
$vcarr[] = "N:".$resarr["myfullname"].";;;;";
//$vcarr[] = "FN:".trim($xml->name);
$vcarr[] = "ORG:".$resarr["myorg"];
$vcarr[] = "TITLE:".$resarr["myoffice"];
$vcarr[] = "TEL;TYPE=WORK,VOICE:".$resarr["myphone"];
$vcarr[] = "TEL;TYPE=CELL,VOICE:".$resarr["mymobile"];
$vcarr[] = "ADR;TYPE=WORK,PREF:;;".$resarr["myaddress"];
$vcarr[] = "EMAIL:".$resarr["myemail"];
$vcarr[] = "END:VCARD";

$vctext = implode(PHP_EOL,$vcarr);

if (preg_match('/[א-ת]/',$vctext)){ //for hebrew
    $vctext = iconv("UTF-8", "windows-1255", $vctext);
}

echo base64_encode($vctext);

?>








