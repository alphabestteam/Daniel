//1
const helloWorld = () =>{
     return "Hello World";
}
console.log(helloWorld());
//2
const helloName = (name) =>{
    return "Hello " + name;
}
console.log(helloName("Daniel"));
//3
const square = (num) => Math.pow(num, 2)
console.log(square(5));

//4
const rectangle = (length,width) => length * width
console.log(rectangle(5,2))
//5
function circleCalculate(radius) {
    const circumference = 2 * Math.PI * radius;
    const area = Math.PI * Math.pow(radius,2);
    return [circumference, area];
}
console.log(circleCalculate(1));
//6
const countVowels = (text) => {
    let matches = text.match(/[aeiouAEIOU]/gi);
    if (matches === null || matches.length === 0) {
        return "There are no vowels in the text";
    }
    return matches.length;
}
console.log(countVowels("tt")); 


//7
const arrayLengths = (arr1, arr2) => arr1.length==arr2.length
console.log(arrayLengths([1,2],[2,3,2]));

//8
const convertNumberToArray = (number) => {
    const numArr = [];
    const strNumber = number.toString();
    for (let i = 0; i < strNumber.length; i++) {
        const toNum = strNumber.charAt(i);
        numArr.push(parseInt(toNum));
    }
    return numArr;
}
console.log(convertNumberToArray(432324));
//9
const getTrueAndFalse = (arr) => {
    const trueFalse = []
    for (let i = 0; i < arr.length; i++) { 
        if (arr[i]){
            trueFalse.push(true)
        }else trueFalse.push(false)
    }
    return trueFalse;
}
const myArr = [1, "hello", true, 0, false, "", " ", null, undefined, NaN, 
2, "world", true, {}, [], 3, "foo", 'true', 'false', "bar"];
console.log(getTrueAndFalse(myArr));
