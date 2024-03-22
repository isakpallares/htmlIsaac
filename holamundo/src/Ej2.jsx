function Ej2() {
    let nombre = "";
    let asistencia = "";
    const nombreTarget = (e) => {
        nombre = e.target.value
    }
    const asistenciaTarget = (e) => {
        asistencia = e.target.value
    }
    const guardar = (e) => {
        const name = nombre;
        const asis = asistencia
        if(name.length == 0 || asis.length == 0){
            alert("No hay ningun dato")
        }else{
            alert("El estado del estudiante: "+ name + " Es: " + asis)
        }
        
    }
    return (
        <>
            <form action="">
                <label for="nombreEstudiante">Nombre del Estudiante:</label>
                <input type="text" name="nombre" step="0.01" required onChange={nombreTarget}/><br /><br />
                <label for="Asistencia">Asistencia: </label>
                <input type="text" name="asistencia" step="0.01" required onChange={asistenciaTarget}/><br /><br />
                <button type="submit" class="boton" onClick={guardar} >Guardar Cambios</button>
            </form>
        </>
    )

}

export default Ej2;