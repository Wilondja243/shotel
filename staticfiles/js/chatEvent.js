const input_message = document.getElementById("message");

input_message.addEventListener('input', (e)=>{
    e.preventDefault()
    const sender = document.querySelector(".chat-form button");

    if(
        input_message.value.trim().length > 0 &&
        sender.classList.contains("bi-send")
    ){
        sender.classList.remove("bi-send");
        sender.classList.add("bi-send-fill");
        sender.style.setProperty("color", "#4EB5AC");
    }
    else{
        sender.classList.remove("bi-send-fill");
        sender.classList.add("bi-send");
        sender.style.removeProperty("color", "#4EB5AC");
    }
})
