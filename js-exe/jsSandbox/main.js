// 1
const mainHeading = document.getElementById("main-heading");

// 2
console.log(mainHeading.id);

// 3
console.log(mainHeading.className);

// 4
console.log(mainHeading.classList);

// 5
console.log(mainHeading.dataset);

// 6
console.log(mainHeading.getAttribute("nonstandard"));

// 7
mainHeading.classList.add("border");
mainHeading.classList.add("bg-lightcyan"); 

// 8
console.log(mainHeading.textContent);

// 9
console.log(mainHeading.textContent.trim());

// 10
mainHeading.textContent = "Hello there, Pearl!"; 
// 11
const span = document.createElement("span");
span.innerText = "It's me, SpongeBob!"; 

// 12
console.log(mainHeading.textContent);

// 13
const cloned = mainHeading.cloneNode(true);
console.log(cloned);

// 14
const string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

// 15
let strArr = string.split(" ");

// 16
const colors = [
  "red",
  "orange",
  "yellow",
  "greenyellow",
  "lightblue",
  "mediumpurple"
];

// 17
function randomColor() {
  const randomIndex = Math.floor(Math.random() * colors.length);
  return colors[randomIndex];
}

// 18
const randomWordSection = document.getElementById("random-words");

// 19
strArr.forEach((word) => {
  const span = document.createElement("span");
  const style = "background-color: " + randomColor();

  span.setAttribute("style", style);
  span.textContent = word;
  span.className = "random-word";

  randomWordSection.appendChild(span);
});
