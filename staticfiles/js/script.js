
async function getUser(){
    try{
        const res = await fetch('http://127.0.0.1:8000/api/v1/users/',{
            method: "GET",
            headers: {
                "Accept": "application/json",
                "Authorization": "Token 5c10552c88541440dd80ef5d5f2e8dafec0698fd"
            }
        })

        if(!res.ok) throw new Error("erreur de chargement");

        const data = await res.json();

        console.log(`data: ${JSON.stringify(data, null, 4)}`)

        data.forEach(d =>{
            const tbody = document.querySelector("table tbody");
            tbody.innerHTML += `
                <tr>
                    <td>${d.username}</td>
                    <td>${d.email}</td>
                    <td>${d.url}</td>
                </tr>
            `
        })

        return data;
    }
    catch(error) {
        console.error("Operation error:", error.message);
    }
}

document.addEventListener("DOMContentLoaded", ()=>{
    getUser()
})
