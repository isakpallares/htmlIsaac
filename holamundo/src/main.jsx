import React from 'react'
import "./main.css"
import {BrowserRouter,Route, Routes} from "react-router-dom"
import ReactDOM from 'react-dom/client'
import Pokemon from './videoLearning/components/Pokemon'
import PokemonList from './videoLearning/components/PokemonList'
import Navbar from './proyectoVideo/components/Navbar'
import ItemListContainer from './proyectoVideo/components/ItemListContainer'
import ItemDetailContainer from './proyectoVideo/components/ItemDetailContainer'
import Nosotros from './proyectoVideo/components/Nosotros'
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<ItemListContainer/>} />
        <Route path="/item/:id" element={<ItemDetailContainer />} />
        <Route path="/productos/:categoria" element={<ItemListContainer />} />
        <Route path="/nosotros" element={<Nosotros/>} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
