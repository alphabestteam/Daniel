
const mainHeading = document.getElementById("main-heading");

console.log(mainHeading.id);

console.log(mainHeading.className);

console.log(mainHeading.classList);

console.log(mainHeading.dataset);
console.log(mainHeading.getAttribute("nonstandard"));

mainHeading.classList.add("border", "bg-lightcyan");

mainHeading.textContent;

mainHeading.textContent.trim();

mainHeading.textContent = "“Hello there pearl!";

const span = document.createElement("span");
span.innerText = "its me SpongeBob!";

mainHeading.textContent;

const cloned = mainHeading.cloneNode(true);
console.log(cloned);

const subheading = document.createElement("h2");
subheading.textContent = "jellyfish hunting is the best";

document.body.appendChild(subheading);

const string ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

const strArr = string.split(" ");
console.log(strArr);


const randomWord = document.getElementById("random-words");

strArr.forEach((word) => {
    const span = document.createElement("span");
    const style = "background-color: " + randomColor();
  
    span.setAttribute("style", style);
    span.textContent = word;
    span.className = "random-word";
  
    randomWord.appendChild(span);
});


//////////////////////////// 14 ////////////////////////////////////////


function randomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    const color = `rgb(${r}, ${g}, ${b}`; 
    return color;
  }
  
const changeColorButton = document.getElementById("change-color-button");

changeColorButton.addEventListener("click", () => {
const randomWordElements = document.querySelectorAll(".random-word");

  randomWordElements.forEach((element) => {
    element.style.backgroundColor = randomColor();
  });
});


