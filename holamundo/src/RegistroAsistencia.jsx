import React, { useState } from 'react';
import './asistencia.css'
function RegistroAsistencia() {
  const [nombre, setNombre] = useState('');
  const [asistencia, setAsistencia] = useState('');

  const nombreChange = (event) => {
    setNombre(event.target.value);
  };

  const asistenciaChange = (event) => {
    setAsistencia(event.target.value);
  };

  return (
    <div>
      <h2>Registro de Asistencia</h2>
      <form>
        <div>
          <label htmlFor="nombre">Nombre del estudiante:</label>
          <input
            type="text"
            id="nombre"
            value={nombre}
            onChange={nombreChange}
          />
        </div>
        <div>
          <label htmlFor="asistencia">Estado de asistencia:</label>
          <select
            id="asistencia"
            value={asistencia}
            onChange={asistenciaChange}
          >
            <option value="">Seleccionar estado</option>
            <option value="presente">Presente</option>
            <option value="ausente">Ausente</option>
          </select>
        </div>
      </form>
      <div id='estudiante'>
        <h3>Datos ingresados:</h3>
        <p>Nombre: {nombre}</p>
        <p>Estado de asistencia: {asistencia}</p>
      </div>
    </div>
  );
}

export default RegistroAsistencia;
