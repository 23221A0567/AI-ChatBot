const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send");
const typing = document.getElementById("typing");
const themeBtn = document.getElementById("themeBtn");
const voiceBtn = document.getElementById("voice");

// Add message
function addMessage(text, sender) {

    const div = document.createElement("div");
    div.className = sender;

    const span = document.createElement("span");
    span.innerHTML = text;

    div.appendChild(span);

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message
async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    input.value = "";

    typing.style.display = "block";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        setTimeout(() => {

            typing.style.display = "none";

            addMessage(data.reply, "bot");

        }, 800);

    }

    catch (err) {

        typing.style.display = "none";

        addMessage("Server Error!", "bot");

    }

}

// Send Button
sendBtn.onclick = sendMessage;

// Enter Key
input.addEventListener("keypress", function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});

// Suggested Questions
document.querySelectorAll(".suggestion").forEach(btn=>{

    btn.addEventListener("click",()=>{

        input.value = btn.innerText;

        sendMessage();

    });

});

// Dark Mode
themeBtn.onclick=function(){

    document.body.classList.toggle("dark");

}

// Voice Input
if ('webkitSpeechRecognition' in window) {

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-IN";

    recognition.continuous = false;

    recognition.interimResults = false;

    voiceBtn.onclick = function(){

        recognition.start();

    }

    recognition.onresult = function(event){

        input.value = event.results[0][0].transcript;

        sendMessage();

    }

}