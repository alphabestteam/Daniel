function addEvent() {
  const counterDisplay = document.getElementById("counter-display");
  const button = document.getElementById("my-button");

  const incrementCounter = (function () {
    let counter = 0;
    return function () {
      counter++;
      counterDisplay.innerText = counter;
    };
  })();

  button.addEventListener("click", incrementCounter);
}

addEvent();
