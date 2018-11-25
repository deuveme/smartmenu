/*$('#photomod').show();
$('#preview').hide();
$('#success').hide();
$('#prime').hide();*/

var first = 0;
var tiene = 0;

function tieneSoporteUserMedia() {
    return !!(navigator.getUserMedia || (navigator.mozGetUserMedia || navigator.mediaDevices.getUserMedia) || navigator.webkitGetUserMedia || navigator.msGetUserMedia)
}

function _getUserMedia() {
    return (navigator.getUserMedia || (navigator.mozGetUserMedia || navigator.mediaDevices.getUserMedia) || navigator.webkitGetUserMedia || navigator.msGetUserMedia).apply(navigator, arguments);
}
var $video = document.getElementById("video"),
    $canvas = document.getElementById("canvas"),
    $boton = document.getElementById("boton"),
    $estado = document.getElementById("estado");
        $video.srcObject = stream;
        $video.play();
if (tieneSoporteUserMedia()) {
    _getUserMedia({
            video: true
        },
        function (stream) {
            console.log("Permiso concedido");

            //Escuchar el click
            $boton.addEventListener("click", function () {

                //Pausar reproducción
                $video.pause();

                //Obtener contexto del canvas y dibujar sobre él
                var contexto = $canvas.getContext("2d");
                $canvas.width = $video.videoWidth;
                $canvas.height = $video.videoHeight;
                contexto.drawImage($video, 0, 0, $canvas.width, $canvas.height);

                var foto = $canvas.toDataURL(); //Esta es la foto, en base 64
                $estado.innerHTML = "Enviando foto. Por favor, espera...";
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "./guardar_foto.php", true);
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.send(encodeURIComponent(foto)); //Codificar y enviar

                xhr.onreadystatechange = function () {
                    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
                        console.log("La foto fue enviada correctamente");
                        console.log(xhr);
                        $estado.innerHTML = "Foto guardada con éxito. Puedes verla <a target='_blank' href='./" + xhr.responseText + "'> aquí</a>";
                    }
                }

                //Reanudar reproducción
                $video.play();
            });
        },
        function (error) {
            console.log("Permiso denegado o error: ", error);
            $estado.innerHTML = "No se puede acceder a la cámara, o no diste permiso.";
        });
} else {
    alert("Lo siento. Tu navegador no soporta esta característica");
    $estado.innerHTML = "Parece que tu navegador no soporta esta característica. Intenta actualizarlo.";
}


/*
// Declaramos elementos del DOM
var $video = document.getElementById("video"),
    $canvas = document.getElementById("canvas"),
    $boton = document.getElementById("boton"),
    $estado = document.getElementById("estado");

if (tieneSoporteUserMedia()){
    _getUserMedia(
        {video: true},
        function (stream) {
            console.log("Permiso concedido");	

            //Escuchar el click
            $boton.addEventListener("click", function(){

                //Pausar reproducción
                $video.pause();

                //Obtener contexto del canvas y dibujar sobre él
                var contexto = $canvas.getContext("2d");
                $canvas.width = $video.videoWidth;
                $canvas.height = $video.videoHeight;
                contexto.drawImage($video, 0, 0, $canvas.width, $canvas.height);

                var foto = $canvas.toDataURL(); //Esta es la foto, en base 64
                document.getElementById('scan-file').value = foto;
                console.log("done")
                console.log(foto)
                /*
                $estado.innerHTML = "Enviando foto. Por favor, espera...";
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "./guardar_foto.php", true);
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.send(encodeURIComponent(foto)); //Codificar y enviar

                xhr.onreadystatechange = function() {
                    if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
                        console.log("La foto fue enviada correctamente");
                        console.log(xhr);
                        $estado.innerHTML = "Foto guardada con éxito. Puedes verla <a target='_blank' href='./" + xhr.responseText + "'> aquí</a>";
                    }
                }*/

                //Reanudar reproducción
                /*$video.play();
            });
        }, function (error) {
            console.log("Permiso denegado o error: ", error);
            $estado.innerHTML = "No se puede acceder a la cámara, o no diste permiso.";
});
} else {
    alert("Lo siento. Tu navegador no soporta esta característica");
    $estado.innerHTML = "Parece que tu navegador no soporta esta característica. Intenta actualizarlo."; 
}/*
function osdfgh(){
    if(first == 0){
        if (tieneSoporteUserMedia()) {
            _getUserMedia({
                    video: true
                },
                function (stream) {
                    $('#photomod').show();
                    first = 1;
                    console.log("Permiso concedido");
                    $video.srcObject = stream;
                    $video.play();
                },
                function (error) {
                    console.log("Permiso denegado o error: ", error);
                    $estado.innerHTML = "No se puede acceder a la cámara, o no diste permiso.";
                });
        } else {
            alert("Lo siento. Tu navegador no soporta esta característica");
            $estado.innerHTML = "Parece que tu navegador no soporta esta característica. Intenta actualizarlo.";
        }
    } else {
        first = 0;
        //Pausar reproducción
        $video.pause();

        //Obtener contexto del canvas y dibujar sobre él
        var contexto = $canvas.getContext("2d");
        $canvas.width = $video.videoWidth;
        $canvas.height = $video.videoHeight;
        contexto.drawImage($video, 0, 0, $canvas.width, $canvas.height);

        var foto = $canvas.toDataURL(); //Esta es la foto, en base 64
        document.getElementById('scan-file').value = foto;
        console.log("done")
        console.log(foto)
        $('#photomod').hide();
        $('#success').show();
        $('#prime').hide();
        /*$estado.innerHTML = "Enviando foto. Por favor, espera...";
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "./guardar_foto.php", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send(encodeURIComponent(foto)); //Codificar y enviar

        xhr.onreadystatechange = function () {
            if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
                console.log("La foto fue enviada correctamente");
                console.log(xhr);
                $estado.innerHTML = "Foto guardada con éxito. Puedes verla <a target='_blank' href='./" + xhr.responseText + "'> aquí</a>";
            }
        }
        */

        //Reanudar reproducción
        /*$video.play();
    }
}*/

function uploadfile(){
    var preview = document.querySelector('img'); //selects the query named img
    var file = document.querySelector('input[type=file]').files[0]; //sames as here
    var reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
        console.log(reader.result)
        document.getElementById('scan-file').value = reader.result;
        console.log(document.getElementById('scan-file').value)
        print("done");
        $('#success').show();
        $('#prime').hide();        
    }

    if (file) {
        console.log("oli")
        reader.readAsDataURL(file); //reads the data as a URL
    } else {
        preview.src = "";
    }
}
