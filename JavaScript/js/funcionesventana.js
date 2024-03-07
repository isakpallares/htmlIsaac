
        function abrir(){
            let ventana = window.open();
            ventana.document.write("Texto escrito en la nueva ventana <br>")
            ventana.document.write("Texto escrito en la seguda linea")
        }
        function abrirConParametros(){
            let ventana = open("","","width = 400, height=250, menubar=yes");
            ventana.document.write("Texto escrito")
        }
        function confirmar(){
            let respuesta = confirm("Está seguro: ")
            if(respuesta == true){
                
                window.location="https://zonacero.com/";
            }else{
                alert("Presionó cancelar")
            }
        }
        