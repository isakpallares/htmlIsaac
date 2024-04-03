import { useState } from "react"
import ListadoResultados from "./ComponenteOperacionesListado";
import './index.css'

function OperacionesApp(){
    const [operaciones, setOperacion]=useState([]);
    
    function sumar(event){
        event.preventDefault();
        const v1 = parseInt(document.getElementById("valor1").value);
        const v2 = parseInt(document.getElementById("valor2").value);
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
        const v1 = parseInt(document.getElementById("valor1").value);
        const v2 = parseInt(document.getElementById("valor2").value);
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
    function multiplicar(event){
        event.preventDefault();
        const v1 = parseInt(document.getElementById("valor1").value);
        const v2 = parseInt(document.getElementById("valor2").value);
        const suma = v1 * v2;
        const nuevo ={
            resultado : suma,
            valor1 : v1,
            valor2 : v2
        }
        setOperacion([nuevo,...operaciones]);
        event.target.valor1.value=''
        event.target.valor2.value=''
    }
    function dividir(event){
        event.preventDefault();
        const v1 = parseInt(document.getElementById("valor1").value);
        const v2 = parseInt(document.getElementById("valor2").value);
        const dividir = v1 / v2;
        const nuevo ={
            resultado : dividir,
            valor1 : v1,
            valor2 : v2
        }
        setOperacion([nuevo,...operaciones]);
        event.target.valor1.value=''
        event.target.valor2.value=''
    }
    return(
        <div>
            <form>
                <p>Ingrese primer valor: <input type="text" name="valor1" id="valor1"/></p>
                <p>Ingrese Segundo valor: <input type="text" name="valor2" id="valor2"/></p>
                <input type="submit" id="suma" onClick={sumar} value="sumar" />
                <input type="submit" id="resta" onClick={restar}  value="restar" />
                <input type="submit" id="multi" onClick={multiplicar} value="Multiplicar" />
                <input type="submit" id="divi" onClick={dividir} value="Dividir" />
            </form>
            <ListadoResultados resultados = {operaciones} />
        </div>
    )
}
export default OperacionesApp