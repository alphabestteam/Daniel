//3
const mainHeading = document.getElementById("main-heading");
//4
console.log(mainHeading.id);
//5
console.log(mainHeading.className)
//6
console.log(mainHeading.classList);
//7
console.log(mainHeading.dataset)
console.log(mainHeading.getAttribute("nonstandard"))
//8
mainHeading.classList.add("border");
mainHeading.classList.add(".bg-lightcyan");
//9
mainHeading.textContent
//10
mainHeading.textContent.trim()
//11
mainHeading.textContent= "“Hello there pearl!"
//12
const span = document.createElement('span') 
span.innerText = "its me SpongeBob!"
//13
mainHeading.textContent
//14
const cloned = mainHeading.cloneNode(true);
cloned
//15


//17
const string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
//18
string.split(" ")
//19
const colors = ["red", "orange", "yellow", "greenyellow", "lightblue", "mediumpurple"]
//20
function randomColor() {
    const randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];
}
//21
const word = document.getElementById("random-words")
//22 /23

strArr.forEach((word) => {
    const span1 = document.createElement("span");
    const style = "background-color: " + randomColor();
  
    span1.setAttribute("style", style);
    span1.textContent = word;
    span1.className = "random-word";
  
    randomWord.appendChild(span1);
  });