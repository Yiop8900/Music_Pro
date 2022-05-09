function validarNombre() {
    var nombre= document.getElementById("txtNombre").value;
    if (nombre.trim().length==0) {
        alert("El nombre no puede estar en blanco.");
   
        return false;
    }
    return true;
    
}