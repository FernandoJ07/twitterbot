function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function editTweet(id){

    fetch(`edit/${id}`, {
        method: 'POST',
        body: JSON.stringify({
            title: document.querySelector(`#titleForm-${id}`).value,
            content: document.querySelector(`#contentForm-${id}`).value,
            date: document.querySelector(`#dateForm-${id}`).value
        }),
        headers: {'X-CSRFToken': getCookie('csrftoken'),} 
    })
    .then(response => response.json())
    .then((tweet) => {
        document.querySelector(`#title-${id}`).innerHTML = tweet.title
        document.querySelector(`#content-${id}`).innerHTML = tweet.content
        document.querySelector(`#date-${id}`).innerHTML = `Fecha de envío: ${tweet.date}`
    })


}