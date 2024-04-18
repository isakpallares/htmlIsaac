import { useEffect, useState } from "react"
import { pedirDatos } from "../helpers/pedirDatos"
import ItemList from "./ItemList"
import { useParams } from "react-router-dom"
import {collection,getDocs, query, where} from "firebase/firestore"
import { db } from "../../firebase/config"

const ItemListContainer = () => {
    //Aquí se traen los datos de data.json, manejar la logica y setear su estado
    const [productos,setProductos] = useState([])
    const [titulo,setTitulo] = useState("Prod uctos");
    const categoria = useParams().categoria;
    useEffect(() => {
    //referencia a la base de datos
      const productosRef = collection(db,"productos")
      
      const q = categoria ? query(productosRef, where("categoria", "==", categoria)) : productosRef;
      
      getDocs(q)
        .then((resp)=> {
            setProductos(
                resp.docs.map((doc)=>{
                    return {...doc.data(), id : doc.id}
                })
             )
        })
    }, [categoria])

    return (
        <ItemList productos={productos} titulo={titulo}/>
    )
}

export default ItemListContainer