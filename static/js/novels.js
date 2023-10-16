   function showPopup(popupId) {
  document.getElementById(popupId).style.display = "flex";
}

// Function to close a specific popup
function closePopup(popupId) {
  document.getElementById(popupId).style.display = "none";
}

// Add event listeners to each "Show Popup" button
const showPopupButtons = document.querySelectorAll(".showPopupButton");
showPopupButtons.forEach((button, index) => {
  button.addEventListener("click", () => {
      showPopup(`popupContainer${index + 1}`);
  });
});