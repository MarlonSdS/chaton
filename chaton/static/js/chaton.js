const chatMessages = qs(".messages")

const setRoomActive = (room_id) => {
    qsa(".list-room li").forEach((el)=> el.classList.remove("active"))
    qs(`#room-${room_id}`).classList.add("active")
    const input = qs('input[name="room_id"]')
    input.setAttribute('value', `${room_id}`)
}

const getMessages = async (room_id) => {
    const response = await fetch(`${room_id}`)
    const html = await response.text()
    chatMessages.innerHTML = html
    setRoomActive(room_id)
}

const sendMessage = async (data) =>{
    console.log(data)
    const response = await fetch(`${data.room_id}/send`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": data.csrfmiddlewaretoken,
        },
        body: JSON.stringify(data)
    })
    const html = await response.text()
    console.log(html)
    const uniqueMessageContainer = qs('.unique-message-container')
    uniqueMessageContainer.insertAdjacentHTML('beforeend', html)
    const form = qs("form")
    form.reset();
}

const form = qs('.send-message');
form.addEventListener("submit", (ev) => {
    ev.preventDefault()
    const data = Object.fromEntries(new FormData(ev.target).entries())
    sendMessage(data)
})

getMessages(1)