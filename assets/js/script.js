
export class FetchUserData{

    constructor(){
        // this.getUser();
        // this.getFollowers();
    }

    async getUser(){
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

            // console.log(`data: ${JSON.stringify(data, null, 4)}`)

            data.forEach(d =>{
                const tbody = document.querySelector("table tbody");
                if(tbody){
                    tbody.innerHTML += `
                        <tr>
                            <td>${d.username}</td>
                            <td>${d.email}</td>
                            <td>${d.url}</td>
                        </tr>
                    `
                }
                
            })

            return data;
        }
        catch(error) {
            console.error("Operation error:", error.message);
        }
    }

    // async getFollowers(){
    //     try{
    //         const res = await fetch("http://127.0.0.1:8000/api/v1/followers/",{
    //             method: "GET",
    //             headers: {
    //                 "Accept": "application/json",
    //             }
    //         })

    //         if(!res.ok) throw new Error("erreur de chargement");
    //         const data = await res.json();

    //         console.log(`Followers: ${JSON.stringify(data.objects, null, 4)}`)

    //         data.objects.followers.forEach(follower => {
    //             let follower_list = document.getElementById("follower_list");

    //             if(follower_list){
    //                 follower_list.innerHTML += `
    //                     <div class="item">
    //                         <div>
    //                             <div class="profil">
    //                                 <img src="{% static 'images/default_profil.jpg' %}">
    //                             </div>
    //                             <div>
    //                                 <b>Luckson Premier</b>
    //                                 <small>Bujumbura Burundi</small>
    //                             </div>
    //                         </div>
    //                         <a href="{% url 'chat' %} class="bi bi-chat-door btn"></a>
    //                     </div>
    //                 `
    //             }
    //         })
    //     }
    //     catch(error){
    //         console.error("Operation error:", error.message)
    //     }
    // }

    async addFriend(friendId) {
        const addButton = document.getElementById("add" + friendId);
        const csrfToken = this.getCsrfToken();

        try{
            const res = await fetch("http://127.0.0.1:8000/home/friends/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ 'friend_id': 1,})
            })

            if(!res.ok) throw new Error("erreur de chargement");
            const data = await res.json();

            console.log(JSON.stringify(data[0].is_my_follower), null, 4)

            // console.log(JSON.stringify(data), null, 4)

            // data.forEach(d =>{
            //     console.log(JSON.stringify(d))
            // })
            
            // .then(data => {

            //     console.log("Données reçues du serveur : ", data);

            //     if (data.status === "added") {
            //         addButton.textContent = "Added";
            //     } else if (data.status === "removed"){
            //         addButton.textContent = "Add friend";
            //     }
            // })

        }catch(error ){
             console.error("Erreur lors du fetch : ", error)
        };
    }

    getCsrfToken() {
        let csrfToken = null;
        const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
        if (csrfCookie) {
            csrfToken = csrfCookie.split('=')[1];
        }
        return csrfToken;
    }
}



