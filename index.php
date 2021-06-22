<?php 
    require "./model/db.php";
    include_once "./control/logfile.php";

    $dbcon = new db();
    $dbcon->connect();

    $username = $_GET["q"];
    $cleanusername = $dbcon->clean(strtolower($username));

    $resarr = $dbcon->selectuser($cleanusername);

    $name_in = $resarr["myfullname"];
    $office_in = $resarr["myoffice"];
    $org_in = $resarr["myorg"];
    $tel_in = $resarr["myphone"];
    $cell_in = $resarr["mymobile"];
    $email_in = $resarr["myemail"];
    $site_in = $resarr["mywebsite"];
    $address_in = $resarr["myaddress"];

?>
<!doctype html>
<html>
<head>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  
    <title>Visit Card</title>
  
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <script src="vvc.js"></script>

    <style>
        a {
            text-decoration: none;
            color:rgb(38, 3, 119);
        }
        .textfont {
            font-weight: normal;
        }
        @media screen and (max-width: 600px) {
        .textfont {
            font-weight: bold;
        }
        }
        .w3-table td, .w3-table th{
            padding:8px 8px;
            display:table-cell;
            text-align:left;
            vertical-align:top;
        }

    </style>

</head>

<body dir="ltr" style="font-size: 1.2em;">
    <div class='bc-img'>
        <img src='logo.jpg' alt='Muni Logo' style="position: absolute; text-align:center; opacity:0.2;z-index:-1;">
    </div>
    <div class="w3-card-4">
        <header class="w3-container">
            <h3 style="text-align:center" id="username" data-username="<?php echo $username; ?>"><?php echo $name_in.', '.$office_in; ?></h3>
        </header>

        <div class="w3-container">    
            <table class="w3-table">
                <tr>
                    <td>
                        Organization
                    </td>
                    <td class="textfont"><?php echo $org_in; ?></td>
                </tr>
                
                <tr>
                    <td>
                        Phone
                    </td>
                    <td class="textfont"><a href="tel:<?php echo $tel_in; ?>"><?php echo $tel_in; ?></a></td>
                </tr>
                
                <tr>
                    <td>
                        Cellphone 
                    </td>
                    <td class="textfont"><a href="tel:<?php echo $cell_in; ?>"><?php echo $cell_in; ?></a></td>
                </tr>
                
                <tr>
                    <td>
                        Email
                    </td>
                    <td class="textfont"><a href="mailto:<?php echo $email_in; ?>"><?php echo $email_in; ?></a></td>
                </tr>
                
                <tr>
                    <td>
                        Website
                    </td>
                    <td class="textfont"><a href="http://<?php echo $site_in; ?>"><?php echo $site_in; ?></td>
                </tr>
                
                <tr>
                    <td>
                        Address
                    </td>
                    <td class="textfont"><a href="https://www.openstreetmap.org/search?query=<?php echo $address_in; ?>" target="_blank"><?php echo $address_in; ?></a></td>
                </tr>
    
            </table>    
        </div>  
    
        <footer class="w3-container w3-row">
        <p>
            <input height = "100px" type="button" class="btn w3-sand w3-round-large w3-large w3-mobile" value="Make QR code" onclick="vvc.qrcode()">
            
            <input type="button" class="btn w3-sand w3-round-large w3-large w3-mobile" value="Download vc" onclick="vvc.vcard()">
    
            <input type="button" class="btn w3-sand w3-round-large w3-large w3-mobile" value="Share" onclick="vvc.vshare()">
        </p>
    
        </footer>
    
    </div>
    
</body>

</html>