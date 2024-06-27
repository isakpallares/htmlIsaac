import react,{ useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld(){
  const [message, setMessage] = useState('');
  
  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/hola/hello-world/')
      .then(response=>{
        setMessage(response.data.message);
        console.log('Respuesta recibida');
      })
      .catch(error=>{
        console.log(error);
      })
  },[])
  
  return(
    <div>
      <p>{message}</p>
    </div>
  );
}
export default HelloWorld;