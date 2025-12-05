const socket = new WebSocket("ws://127.0.0.1:8000/ws/api/test/");

socket.onopen = () => {
    console.log("Connected !")

    socket.send(JSON.stringify({"message": "Bonjour serveur"}));

}

socket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    console.log("Message recu : ", data)

    const content = document.getElementById("content");

    content.textContent = data.message;
}
