import { useEffect, useState } from "react";

const TextH2 = () => {
    const [text,setText] = useState("")
    const handleText = (e) => {
        setText(e.target.value);
    }
    useEffect(()=>{
        console.log("Componente montado!")
        return () => {
            console.log("Componente Desmontado!")
        }
    }, []);
    return (
        <div>
            <input type="text" onChange={handleText}/>
            <p>{text}</p>    
        </div>
    
    )
}
export default TextH2;