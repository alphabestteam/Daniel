const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
        console.log("SpongBob caught a " + jellyfish.color + " jellyfish");
        identifyJellyfishAndAddPoints(jellyfish, addPoints)
        console.log("Score: " +score);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    if (jellyfish.color == "pink") {
        addPoints("pink spotted");
        console.log("Patrick identified: pink spotted jellyfish");
    } else if (jellyfish.color == "blue") {
        addPoints("blue stinger");
        console.log("Patrick identified: blue stinger jellyfish");
    } else if (jellyfish.color == "green") {
        addPoints("green itches");
        console.log("Patrick identified: green itches jellyfish");
    } else {
        console.log("Patrick identified: common jellyfish");
    }
}

// Score keeping callback function
function addPoints(species) {
    if (speciesPoints[species]) {
        score += speciesPoints[species];
    }
}

for (const day of jellyfishDays) {
    score = 0;
    console.log("Let's go jellyfishing");
    for (const jellyfish of day) {
        catchJellyfish(jellyfish, identifyJellyfishAndAddPoints);
    }
    console.log("Total Score: " + score + "\n");
}