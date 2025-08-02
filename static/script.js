const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

function addMessage(text, className) {
  const message = document.createElement("div");
  message.className = `message ${className}`;
  message.innerText = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = userInput.value;
  if (!message.trim()) return;

  addMessage(`You: ${message}`, "user");
  userInput.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    addMessage(`CoffeeBot: ${data.reply}`, "bot");
  } catch (err) {
    addMessage("Error: Unable to reach CoffeeBot.", "bot");
  }
});
