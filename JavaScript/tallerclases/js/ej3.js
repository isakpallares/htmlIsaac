class CuentaBancaria{
    constructor(titular, saldo){
    this.titular = titular;
    this.saldo = saldo;
    this.depositar = depositar;
    this.retirar = retirar;
    this.obtenerSaldo = obtenerSaldo;
    }
}

function depositar(valor){
    this.saldo = this.saldo + valor;
}

function retirar(valor){
    this.saldo = this.saldo - valor;
}

function obtenerSaldo(){
    document.write("El saldo actual es de: "+this.saldo)
}