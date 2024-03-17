document.getElementById("nombreProducto").addEventListener("change", function() {
    let productoSeleccionado = this.value;
    let precioProducto = 0;
    
    // Definir precios predeterminados para cada producto
    switch(productoSeleccionado) {
      case "Producto 1":
        precioProducto = 356.95;
        break;
      case "Producto 2":
        precioProducto = 471.90;
        break;
      case "Producto 3":
        precioProducto = 163.35;
        break;
      case "Producto 4":
        precioProducto = 163.35;
        break;
      case "Producto 5":
        precioProducto = 326.70;
        break;
      default:
        precioProducto = 0;
    }
    
    document.getElementById("precioProducto").value = precioProducto.toFixed(2);
  });

  document.getElementById("formaCarta").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let nombreProducto = document.getElementById("nombreProducto").value;
    let precioProducto = parseFloat(document.getElementById("precioProducto").value);
    let cantidad = parseInt(document.getElementById("cantidad").value);
    let total = precioProducto * cantidad;
    
    let table = document.getElementById("tablaCarrito").getElementsByTagName('tbody')[0];
    let row = table.insertRow(-1);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);
    let cell6 = row.insertCell(5);
    cell1.innerHTML = nombreProducto;
    cell2.innerHTML = "$" + precioProducto.toFixed(2);
    cell3.innerHTML = cantidad;
    cell4.innerHTML = "$" + total.toFixed(2);
    cell5.innerHTML = "<button class='boton' onclick='editItem(this)'>Modificar</button>";
    cell6.innerHTML = "<button class='boton' onclick='removeItem(this)'>Eliminar</button>";
    updateTotal();
    document.getElementById("formaCarta").reset();
  });

  function editItem(button) {
    let row = button.parentNode.parentNode;
    let cells = row.getElementsByTagName("td");
    let nombreProducto = cells[0].innerHTML;
    let precioProducto = parseFloat(cells[1].innerHTML.substring(1)); // Remove "$" before parsing
    let cantidad = parseInt(cells[2].innerHTML);

    document.getElementById("editarIndice").value = row.rowIndex;
    document.getElementById("editnombreProducto").value = nombreProducto;
    document.getElementById("editprecioProducto").value = precioProducto;
    document.getElementById("editcantidad").value = cantidad;
    document.getElementById("editarContenedorForm").style.display = "block";
  }

  function cancelEdit() {
    document.getElementById("editarContenedorForm").style.display = "none";
  }

  document.getElementById("editarForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let rowIndex = document.getElementById("editarIndice").value;
    let nombreProducto = document.getElementById("editnombreProducto").value;
    let precioProducto = parseFloat(document.getElementById("editprecioProducto").value);
    let cantidad = parseInt(document.getElementById("editcantidad").value);
    let total = precioProducto * cantidad;

    let table = document.getElementById("tablaCarrito");
    let row = table.rows[rowIndex];
    let cells = row.getElementsByTagName("td");
    cells[0].innerHTML = nombreProducto;
    cells[1].innerHTML = "$" + precioProducto.toFixed(2);
    cells[2].innerHTML = cantidad;
    cells[3].innerHTML = "$" + total.toFixed(2);
    updateTotal();

    document.getElementById("editarContenedorForm").style.display = "none";
  });

  function removeItem(button) {
    let row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
    updateTotal();
  }
  function updateTotal() {
    var table = document.getElementById("tablaCarrito");
    var total = 0;
    for (var i = 1; i < table.rows.length - 1; i++) {
      total += parseFloat(table.rows[i].cells[3].innerHTML.substring(1));
    }
    document.getElementById("totalProductos").innerHTML = "$" + total.toFixed(2);
  }

  function confirmarCompra() {
    alert("¡Compra realizada con éxito!");
  }