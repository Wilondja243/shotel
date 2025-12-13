// import { FetchUserData } from "./script.js";

function getCsrfToken() {
    let csrfToken = null;
    const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
        csrfToken = csrfCookie.split('=')[1];
    }
    return csrfToken;
}

async function addFriend(friendId) {
    const popup = document.getElementById("popup");
    const addButton = document.getElementById("add" + friendId);
    const csrfToken = this.getCsrfToken();

    try{
        const res = await fetch("http://127.0.0.1:8000/home/friends/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ 'friend_id': friendId,})
        })

        if(!res.ok) throw new Error("erreur de chargement");
        const data = await res.json();

        

        if(data.following){
            let newData = JSON.parse(data.following);

            console.log("newData:", typeof newData)
            console.group("message", newData.message)

            newData.forEach(d => {
                console.log(d.fields.is_my_follower)

                if(d.fields.is_my_follower){
                    addButton.textContent = setStrage();
                    console.log(addButton.textContent = "Added");
                }
                else{
                    addButton.textContent = "Add Friend";
                }
            });

            popup.classList.add("success");
            document.querySelector(".popup-message i").className = "bi bi-person-check";
            document.querySelector(".popup-message p").textContent = data.message;

            setTimeout(()=> {
                popup.classList.remove("success");
            }, 3000)
        }
        else{
            document.querySelector(".popup-message i").className = "bi bi-person-x";
            
            popup.classList.add("warning");
            document.querySelector(".popup-message p").textContent = data.message;

            setTimeout(()=> {
                popup.classList.remove("warning");
            }, 3000)
        }
    }catch(error ){
        console.error("Erreur lors du fetch : ", error)
    };
}
