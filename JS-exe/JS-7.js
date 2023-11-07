
const friends = ["sandy", "patrick", "squidward", "Mr", "Gray"];
console.log(friends, friends.length);

let newFriend = "Daniel";
friends.push(newFriend);

console.log(friends, friends.length);
friends[0] = "Chen";
console.log(friends);
// In JavaScript, a const declaration for an array only ensures that the reference to the array remains constant,
// allowing you to modify the array's elements while keeping the same reference.
