

function ComponenteJSX() {
    const siglo = 21;
    const persona = {
        nombre: "Juan",
        edad: 34
    }
    function mostrarTitulo(titulo){
        return{
        
        }
    }
    
    const buscadores = ["https://google.com/url?sa=i&url=https%3A%2F%2Fwww.britannica.com%2Ftechnology%2Fprinting-press&psig=AOvVaw3lDQW7t9S-ncnoxMLPWHaj&ust=1709998330115000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKjdkqv-5IQDFQAAAAAdAAAAABAJ","https://www.bing.com/?setlang=es"]
    const aleatorio = () => Math.trunc(Math.random() * 10);
    let edad = 18;
    function mayorEdad(edad){
        if (edad >= 18) {
            return(
                <h1>Es mayor de edad</h1>
            )
        }else{
            return(
                <h1>Es menor de edad</h1>
            )
        }
    }
    return (
        <>
            <h1>Componente JSX</h1>
            <hr />
            <p>Estamos en el siglo {siglo}, {50 - 5}</p>
            <p>{persona.nombre} tiene {persona.edad}</p>
            <h3>Llamando a una función</h3>
            <p>Valor aleatorio generado: {aleatorio()}</p>
            <h3>Buscadores utilizados</h3>
            <a href={buscadores[0]}>Google</a><br />
            <a href={buscadores[1]}>Bing</a><br />
            {mayorEdad(edad)}
            
            
        </>
    )
}

export default ComponenteJSX;
