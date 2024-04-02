import { useState } from "react"
import ListadoResultados from "./ComponenteOperacionesListado";

function OperacionesApp(){
    const [operaciones, setOperacion]=useState([]);
    function operacionesE(){
        if(document.getElementById("suma")){
            sumar()
            console.log("hola")
        } else if (document.getElementById("resta")) {
            restar()
        }
    }
    function sumar(event){
        event.preventDefault();
        const v1 = parseInt(event.target.valor1.value);
        const v2 = parseInt(event.target.valor2.value);
        const suma = v1 + v2;
        const nuevo ={
            resultado : suma,
            valor1 : v1,
            valor2 : v2
        }
        setOperacion([nuevo,...operaciones]);
        event.target.valor1.value=''
        event.target.valor2.value=''
    }
    function restar(event){
        event.preventDefault();
        const v1 = parseInt(event.target.valor1.value);
        const v2 = parseInt(event.target.valor2.value);
        const suma = v1 - v2;
        const nuevo ={
            resultado : suma,
            valor1 : v1,
            valor2 : v2
        }
        setOperacion([nuevo,...operaciones]);
        event.target.valor1.value=''
        event.target.valor2.value=''
    }
    return(
        <div>
            <form onSubmit={operacionesE}>
                <p>Ingrese primer valor: <input type="text" name="valor1" id="valor1"/></p>
                <p>Ingrese Segundo valor: <input type="text" name="valor2" id="valor2"/></p>
                <input type="submit" id="suma" value="sumar" />
                <input type="submit" id="resta" value="restar" />
                <input type="submit" id="multi" value="Multiplicar" />
                <input type="submit" id="divi" value="Dividir" />
            </form>
            <ListadoResultados resultados = {operaciones} />
        </div>
    )
}
export default OperacionesApp