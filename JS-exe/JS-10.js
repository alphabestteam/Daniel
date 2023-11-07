const characterMap = new Map([
  ["Main character", "spongebob"],
  ["Best friend", "patrick"],
  ["pet", "gary"],
  ["word buddy", "squidward"],
  ["manager", "Mr. Krabs"],
  ["teacher", "Mrs. Puff"],
  ["location", "bikini bottom"],
]);

//1
console.log(characterMap);
//2
console.log(Array.from(characterMap.keys()));
//3
console.log(characterMap.get("location"));
//4
console.log(characterMap.size);
//5
characterMap.delete("location");
//6
console.log(characterMap.size);
//7
console.log(characterMap);
//8
console.log(characterMap.has("location"));
