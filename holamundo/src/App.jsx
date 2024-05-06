import "./main.css"
import {BrowserRouter,Route, Routes} from "react-router-dom"
import ReactDOM from 'react-dom/client'
import Pokemon from './videoLearning/components/Pokemon'
import PokemonList from './videoLearning/components/PokemonList'
import Navbar from './proyectoVideo/components/Navbar'
import ItemListContainer from './proyectoVideo/components/ItemListContainer'
import ItemDetailContainer from './proyectoVideo/components/ItemDetailContainer'
import Nosotros from './proyectoVideo/components/Nosotros'
import Contacto from './proyectoVideo/components/Contacto'
import Carrito from './proyectoVideo/components/Carrito'
import { CartProvider } from "./context/CartContext"
import Checkout from "./proyectoVideo/components/Checkout"

function App() {
    
    return (
    <div>
      <CartProvider>
        <BrowserRouter>
          <Navbar/>
          <Routes>
            <Route path="/" element={<ItemListContainer/>} />
            <Route path="/item/:id" element={<ItemDetailContainer />} />
            <Route path="/productos/:categoria" element={<ItemListContainer />} />
            <Route path="/nosotros" element={<Nosotros/>} />
            <Route path="/contacto" element={<Contacto/>} />
            <Route path="/carrito" element={<Carrito/>} />
            <Route path="/checkout" element={<Checkout/>} />
          </Routes>
        </BrowserRouter>
      </CartProvider>
    </div>
    
  )
}

export default App
