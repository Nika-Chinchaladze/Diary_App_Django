var user_id = document.querySelector("#hidden_username").value;
document.querySelector("select").value = user_id;

var user_options = document.getElementsByTagName("option");
for (let i = 0; i < user_options.length; i++) {
    if (user_options[i].value != user_id) {
        user_options[i].style.display = "none";
    }
}
