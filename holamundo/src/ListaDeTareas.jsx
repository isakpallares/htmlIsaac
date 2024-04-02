import React, { useState } from 'react';
import './tarea.css'

function ListaDeTareas() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');

  const agregarTarea = () => {
    if (nuevaTarea.trim() !== '') {
      setTareas([...tareas, nuevaTarea]);
      setNuevaTarea('');
    }
  };

  const eliminarTarea = (index) => {
    const nuevasTareas = [...tareas];
    nuevasTareas.splice(index, 1);
    setTareas(nuevasTareas);
  };

  return (
    <div>
      <h2>Lista de Tareas</h2>
      <form onSubmit={(e) => { e.preventDefault(); }}>
        <input
          type="text"
          value={nuevaTarea}
          onChange={(e) => setNuevaTarea(e.target.value)}
          placeholder="Agregar nueva tarea"
        />
        <button type="button" onClick={agregarTarea}>Agregar</button>
      </form>
      <ul>
        {tareas.map((tarea, index) => (
          <li key={index}>
            {tarea}
            <button id="eliminar" onClick={() => eliminarTarea(index)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaDeTareas;
