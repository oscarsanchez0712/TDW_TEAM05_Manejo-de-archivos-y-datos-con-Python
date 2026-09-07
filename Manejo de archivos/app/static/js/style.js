const form = document.getElementById("formSubir");
const mensaje = document.getElementById("mensaje");
const resultado = document.getElementById("resultado");
const sinResultado = document.getElementById("sinResultado");
const lista = document.getElementById("listaHistorial");

function mostrarResultado(data) {
  sinResultado.classList.add("hidden");
  resultado.classList.remove("hidden");
  resultado.innerHTML = `
    <p>Archivo: ${data.nombre}</p>
    <p>Líneas: ${data.lineas} - Palabras: ${data.palabras} - Caracteres: ${data.caracteres}</p>
    <p>Palabra más frecuente: ${data.palabra_frecuente}</p>
  `;
}

async function cargarHistorial() {
  const res = await fetch("/historial");
  const datos = await res.json();
  lista.innerHTML = datos.map(d =>
    `<li>${d.nombre} - ${d.lineas} líneas, ${d.palabras} palabras (${d.fecha})</li>`
  ).join("") || "<li>Sin archivos aún.</li>";
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const archivo = document.getElementById("inputArchivo").files[0];
  if (!archivo) return;

  const datosForm = new FormData();
  datosForm.append("archivo", archivo);

  const res = await fetch("/subir", { method: "POST", body: datosForm });
  const data = await res.json();

  if (data.error) {
    mensaje.textContent = data.error;
    mensaje.classList.remove("hidden");
    return;
  }

  mensaje.classList.add("hidden");
  mostrarResultado(data);
  cargarHistorial();
  form.reset();
});

cargarHistorial();
