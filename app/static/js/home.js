// RELÓGIO//
const contador = document.getElementById("contador");

function atualizarRelogio() {
    const agora = new Date();
    contador.textContent = agora.toLocaleTimeString("pt-BR");
}

setInterval(atualizarRelogio, 1000);
atualizarRelogio();




lucide.createIcons();

document.addEventListener("DOMContentLoaded", () => {
    const elementos = document.querySelectorAll(
        ".saudacao-container, .relogio, .menu button"
    );

    
    elementos.forEach(el => el.classList.add("fade-in-up"));

    
    elementos.forEach((el, i) => {
        setTimeout(() => {
            el.classList.add("visible");
        }, 200 * i);
    });
});

