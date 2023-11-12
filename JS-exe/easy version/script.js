const quotes = [
  "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
  "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
  "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
  "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
  "The inner machinations of my mind are an enigma. - Patrick Star",
  "I can't hear you, it's too dark in here! - Patrick Star",
  "I'm ugly and I'm proud! - SpongeBob SquarePants",
  "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
  "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
  "Is mayonnaise an instrument? - Patrick Star",
  "Can you give SpongeBob his brain back? - Patrick Star",
  "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
  "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
  "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
  "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
  "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
  "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
  "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
  "SpongeBob: Can I be excused for the rest of my life?",
  "SpongeBob: I'm not just ready, I'm ready Freddy!",
  "SpongeBob: You don't need a license to drive a sandwich.",
  "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
  "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
  "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
  "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end.",
];
const input = document.getElementById("input");
const timeDisplay = document.getElementById("timer");
const quoteDisplay = document.getElementById("quote");
const result = document.getElementById("result");
let intervalId;

// in this function i choose random quote, then created span to each letter, and added it to the quoteDisplay object.
function getRandomQuote() {
  const currentQuote = quotes[Math.floor(Math.random() * quotes.length)];
  let newContent = "";
  for (let i = 0; i < currentQuote.length; i++) {
    let uniqueClass = `letter-${i}`;
    newContent += `<span class="${uniqueClass}">${currentQuote[i]}</span>`;
  }
  quoteDisplay.innerHTML = newContent;
  clearInterval(intervalId);
  timeElapsedSinceButtonPress();
}

// Function to start the game
function startGame() {
  const startBtn = document.getElementById("start-btn");
  startBtn.addEventListener("click", () => {
    getRandomQuote();
    input.setAttribute("max", "quoteDisplay.length");
    timeDisplay.style.display = "block";
    result.innerHTML = "";
    input.value = "";
  });
  checkInput();
}

// Function to handle user input and typing accuracy
function checkInput() {
  input.addEventListener("keydown", function (event) {
    checkEndQuotes(input, quoteDisplay);
    const keyPressed = event.key;
    const inputIndex = input.selectionStart;

    if (keyPressed === quoteDisplay.textContent.charAt(inputIndex)) {
      const currentLetter = document.getElementsByClassName(
        `letter-${inputIndex}`
      )[0];
      currentLetter.style.color = "green";
    } else if (keyPressed !== "Backspace") {
      const currentLetter = document.getElementsByClassName(
        `letter-${inputIndex}`
      )[0];
      currentLetter.style.color = "red";
    }
    if (keyPressed === "Backspace") {
      for (let i = inputIndex - 1; i < quoteDisplay.textContent.length; i++) {
        const previousLetter = document.getElementsByClassName(
          `letter-${i}`
        )[0];
        previousLetter.style.color = "white";
      }
    }
  });
}
// check if the user got to the end of the quotes.
function checkEndQuotes(input, quoteDisplay) {
  if (input.value.length == quoteDisplay.textContent.length - 1) {
    endGame();
  }
}

// function to start the timer and display elapsed time
function timeElapsedSinceButtonPress() {
  const startTime = new Date();
  intervalId = setInterval(function () {
    const currentTime = new Date();
    const elapsedSeconds = Math.round((currentTime - startTime) / 1000);
    timeDisplay.textContent = elapsedSeconds;
  }, 1000);
}

// Function to calculate the wpm
function calculateWPM(numberOfWords, timeInSeconds) {
  const wpm = (numberOfWords / (timeInSeconds / 60)).toFixed(2);
  return wpm;
}

// Function to end the game, display results, and calculate accuracy
function endGame() {
  const totalWords = quoteDisplay.textContent.split(" ").length;
  const seconds = parseInt(timeDisplay.textContent);
  const typedText = input.value;
  const quoteText = quoteDisplay.textContent;
  const typingSpeed = calculateWPM(totalWords, seconds);

  // Calculate accuracy.
  const correctCharacters = typedText
    .split("")
    .filter((char, index) => char === quoteText[index]).length;
  const accuracyPercentage = (
    (correctCharacters / quoteText.length) *
    100
  ).toFixed(2);

  result.style.display = "block";
  result.innerHTML = `<p>Total Words Typed: ${totalWords}</p><p>Time Taken: ${seconds} seconds</p><p> WPM: ${typingSpeed}</p><p>Accuracy: ${accuracyPercentage}%</p>`;
  clearInterval(intervalId);
  timeDisplay.style.display = "none";
}

startGame();
