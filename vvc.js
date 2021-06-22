var vvc = Object();


//**************************************************************************************************** */

vvc.qrcode = function(){

    var url = "https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=" + window.location.href;

    //window.location.assign(url);
    window.open(url);
}

//***************************************************************************************************** */

vvc.vcard = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("q",document.getElementById("username").dataset.username);

    //console.log(document.getElementById("username").dataset.username);

    xhr.open("post","./control/vvcgen.php",true);

    xhr.onreadystatechange=function(){
        
        if(this.readyState==4 && this.status==200){

            //console.log(this.responseText);

             let a = document.createElement("a");

             document.body.appendChild(a);
         
             a.style = "display: none";
         
             a.href = 'data:application/octet-stream;base64,' + this.responseText;

             a.download = document.getElementById("username").innerHTML.replace(", ","_") + ".vcf";
         
             a.click();
         
             document.body.removeChild(a);
        }
    }

    xhr.send(fdata);
}

//****************************************************************************************************** */

vvc.vshare = function(){

    if (navigator.share != undefined){
        if (navigator.share) {
            navigator.share({
                title: 'VC Sharing',
                text: "Link to VC of " + document.getElementById("username").innerHTML,
                url: window.location.href
            })
              .then(() => console.log('Successful share'))
              .catch((error) => console.log('Error sharing', error));
          }    
    }

    else {
        window.alert("Sharing is not available");
    }    
}
