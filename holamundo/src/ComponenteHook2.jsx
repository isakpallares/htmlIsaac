import { useState } from 'react';
import './App.css'

function ComponenteHook2(){
    const[color,setColor] = useState("red")
    return(
        <>
            <h1> My favorite color is: {color}</h1>
            <button onClick={() => setColor("Red")} >Red</button>
            <button onClick={() => setColor("Blue")} >Blue</button>
            <button onClick={() => setColor("Orange")}>Orange</button>
            <button onClick={() => setColor("Brown")}>Brown</button>
        </>
    )
}

export default ComponenteHook2;