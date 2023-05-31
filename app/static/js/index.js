const chatForm = document.getElementById('chat-form');
const messagesDiv = document.getElementById('messages');

chatForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(chatForm);
    const message = formData.get('message');
    appendMessage('User', message);
    sendMessage(message);
    chatForm.reset();
});

function appendMessage(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.innerHTML = `<strong>${role}: </strong>${content}`;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function sendMessage(message) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(message)}`,
    })
    .then(response => response.text())
    .then(data => appendMessage('ChatGPT', data));
}