window.addEventListener('load', async function (event) {
    event.preventDefault()
    let responseblog = await this.fetch('http://127.0.0.1:8000/en/api/blogs/')
    let responseblogData = await responseblog.json()
    let bloglist = this.document.getElementById('blogsveryveryown')
    for (data of responseblogData){
        bloglist.innerHTML += `
        <option value="${data.id}">${data.title}</option>
        `
    }
})

let form = document.getElementById('blog-comment-form')
form.addEventListener('submit', async function (event) {
    event.preventDefault()
    let formData = new FormData(form)
    let response = await fetch('http://127.0.0.1:8000/en/api/comments/', {
        method: 'POST',
        body: formData
    })
})