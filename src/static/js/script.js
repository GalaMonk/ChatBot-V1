// static/js/script.js

document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    appendMessage("Você", userInput, "user");
    document.getElementById("user-input").value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        });

        if (!response.ok) {
            throw new Error("Erro na requisição");
        }

        const data = await response.json();
        appendMessage("Chatbot", data.response, "bot");
    } catch (error) {
        console.error("Erro:", error);
        appendMessage("Chatbot", "Desculpe, ocorreu um erro ao processar sua solicitação.", "bot");
    }
});

function appendMessage(sender, message, type) {
    const chatbox = document.getElementById("chatbox");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", type);
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Permitir enviar mensagem ao pressionar "Enter"
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("send-btn").click();
    }
});
