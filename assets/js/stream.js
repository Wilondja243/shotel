console.log("Start EventSource")

const source = new EventSource("http://127.0.0.1/home/stream/notification/");

source.onopen = (e)=>{
    console.log("Connexion is open:", e);
}

source.onmessage = (e)=>{
    const data = JSON.parse(e.data)[0];
    const fields = data.fields;

    console.log(fields);

    const users = document.querySelector(".users");
    console.log(users)

    users.textContent = fields.username;
}

source.onerror = (e)=>{
    console.log("Error to fetch notification stream:", e)
}

console.log(source)