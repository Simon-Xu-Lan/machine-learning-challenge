var deleteBtns = document.getElementsByClassName("deleteBtn")

var myFunction = function() {
    var id = this.getAttribute("data-id");
    console.log(id);

    axios.post('/trainset', {
            id: id
        })
        .then(function (response) {
            console.log(response)
            window.location.reload()
        })
        .catch(function (error) {
            console.log(error)
        })
};

for (var i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', myFunction, false);
}

