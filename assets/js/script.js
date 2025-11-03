
async function getUser(){
    try{
        const res = await fetch('http://127.0.0.1:8000/api/v1/users/',{
            method: "GET",
            headers: {
                "Accept": "application/json",
                "Authorization": "Token ac8abf823ff359f207e48efa137a65c8fafb54a3"
            }
        })

        if(!res.ok) throw new Error("erreur de chargement");

        const data = await res.json();


        console.log(`data: ${JSON.stringify(data, null, 4)}`)

        const wrapper = document.getElementById("wrapper");

        wrapper.textContent = JSON.stringify(data)

        return data;
    }
    catch(error) {
        console.error("Echec de l'operation getUser:", error.message);
    }
    
}

document.addEventListener("DOMContentLoaded", ()=>{
    getUser()
})
