import { useEffect, useState } from "react"
import { pedirDatos } from "../helpers/pedirDatos"
import ItemList from "./ItemList"
import { useParams } from "react-router-dom"
const ItemListContainer = () => {
    //Aquí se traen los datos de data.json, manejar la logica y setear su estado
    const [productos,setProductos] = useState([])
    const categoria = useParams().categoria;
    useEffect(() => {
      pedirDatos()
        .then((res)=>{
            if(categoria)
            setProductos(res);
        })
    }, [])
    
    
    return (
        <ItemList productos={productos}/>
    )
}

export default ItemListContainer