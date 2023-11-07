const button = document.getElementById("the-button");
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

button.innerText = "Show me bob ;)";
bobGif.style.display = "none";

button.addEventListener("click", function () {
  const showBob = button.getAttribute("data-show-bob");

  if (showBob === "true") {
    bobGif.style.display = "none";
    button.innerText = "Show me bob ;)";
    button.setAttribute("data-show-bob", "false");
  } else {
    bobGif.style.display = "block";
    button.innerText = "Hide Bob!";
    button.setAttribute("data-show-bob", "true");
  }
});
