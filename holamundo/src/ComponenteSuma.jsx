

function ComponenteSuma() {
    let num1 = "";
    let num2 = "";
    
    const cambioValor1 = (e) => {
        num1 = e.target.value;
    }
    const cambioValor2 = (e) => {
        num2 = e.target.value;
    }
    const presionSuma = (e)=>{
        e.preventDefault();
        const suma = parseFloat(num1) + parseFloat(num2);
        alert("La suma es: "+suma);
    }
    const presionMultiplicar = (e) => {
        e.preventDefault();
        const producto = parseFloat(num1) * parseFloat(num2);
        alert("La multiplicación es: "+producto)
    }
    
    return (
        <>
            <form>
                <p>Primer Sumando
                    <input type="number" name='valor1' id='valor1' onChange={cambioValor1} />
                </p>
                <p>Segundo Sumando
                    <input type="number" name='valor2' id='valor2'onChange={cambioValor2} />
                </p>
                <p>
                    <input type="submit" value='Sumar' onClick={presionSuma}/>
                    <input type="submit" value='Multiplicar' onClick={presionMultiplicar}/>
                </p>
            </form>
        </>
    )
}



export default ComponenteSuma;