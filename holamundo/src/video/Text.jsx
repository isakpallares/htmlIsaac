import { useState } from "react";
import TextH2 from "./TextH2";

const Text = () => {
    const [show, setShow] = useState(true);
    
    function HandleShow(){
        setShow(!show);
    }
    
    return (
        <div>
        <hr />
            <button onClick={HandleShow}>{show ? "Ocultar" : "Mostrar"} </button>
            {show ? <TextH2/> : <h2>chao, mundo!</h2>}
        </div>
    )
}
export default Text;