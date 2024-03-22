import { useState } from "react";

function Ej1() {

    const [contador, setContador] = useState(0);

    const aumentarContador = () => {
        setContador(contador + 1);
    }
    const dismuirContador = () => {
        setContador(contador - 1);
    }

    return (
        <>
            <p>El valor del contador es: {contador}</p>
            <button onClick={aumentarContador}>Aumentar</button>
            <button onClick={dismuirContador}>Disminuir</button>
        </>
    )

}

export default Ej1;