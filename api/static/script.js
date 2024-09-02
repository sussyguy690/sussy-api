document.addEventListener("DOMContentLoaded", () => {
  const welcomeMessage = document.querySelector(".welcome-message");

  // Add a class to trigger the transition
  setTimeout(() => {
    welcomeMessage.classList.add("show");
  }, 100);

  document.getElementById("learnMoreBtn").addEventListener("click", () => {
    alert("More information coming soon!");
  });
});
