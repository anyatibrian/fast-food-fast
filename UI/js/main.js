var profile = document.getElementById("profile-pic");
var profileModal = document.getElementById("profile-modal");
var editFordModal = document.getElementById('edit-food-modal');
profile.onclick= function (){
    profileModal.style.display='block';
}
// when the user clicks out side of the modal,close it
window.onclick = function(event) {
    if (event.target == profileModal) {
        profileModal.style.display = "none";
    }
}
function closeModal() {
    profileModal.style.display="none";
    editFordModal.style.display="none";
}
//edit food modal
function Editfoodmodal() {
    editFordModal.style.display='block';
}
