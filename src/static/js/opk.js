$("#imag").hide();
$("#preview").hide();

function uploadfile(){
    var preview = document.querySelector('img'); //selects the query named img
    var file = document.querySelector('input[type=file]').files[0]; //sames as here
    var reader = new FileReader();

    reader.onloadend = function () {
        $("#imag").show();
        $("#preview").show();
        $("#upload").hide();
        preview.src = reader.result;
        document.getElementById('scan-file').value = reader.result;    
    }

    if (file) {
        reader.readAsDataURL(file); //reads the data as a URL
    } else {
        preview.src = "";
    }

}
