function validarUsuario() {
    var nombre= document.getElementById("txtUsuario").value;
    if (nombre.trim().length==0) {
        alert("El nombre de usuario no puede estar en blanco.");
   
        return false;
    }
    return true;
    
}
