// 1 - arr.at = check for array bounds automatically. but a bit slower.
// arr[index] not check for bounds and can cause to error of exceptions out of the bounds

//2
// let getNumCreateArr = (num) =>{
//     let arr = []
//     for (let i = 0; i < num; i++) {
//         arr.push('A')
//     }
//     console.log(arr);
// }
// getNumCreateArr(4)

//3
// let deleteNfromArr = (arr, n) =>{
//     arr.splice(arr.length-n, n);
//     newArr = arr 
//     console.log(newarr);
// }
// const newarr = ["Banana", "Orange", "Apple", "Mango"]
// deleteNfromArr(newarr,2)

//4
// let pushNumber = (arr, numner) =>{
//     arr.unshift(numner);
//     console.log(arr);
// }
// pushNumber([1,2,3],0)

//5
// let connectArr = (arr1,arr2) =>{
//     newArr = arr1.concat(arr2)
//     console.log(newArr);
// }
// connectArr([1,2,3],[4,5,6])

//6
// let toUpper = (str) =>{
//      return str.toUpperCase();
// }
// const string = ["daniel", "ari", "chen", "efi"];
// const newArr = string.map(toUpper);
// console.log(newArr);

//7
// let checkTwoDigits = (odd) => {
//   return odd.toString().length == 2;
// }
// const nums = [32, 33, 16, 40,1,222];
// const result = nums.filter(checkAdult);
// console.log(result);

//8
// let wordIncludes = (arr, word) =>{
//     if (arr.includes(word)){
//         return true
//     }return false
// }
// console.log(wordIncludes(["chen","david","mia"],"m"));

//9
// let findNumber = (arr) => {
//      return arr > 10
// }
// const arr = [1,2,3,4,10,35,10]
// console.log(arr.find(findNumber));

//10
// let isExist = () =>{
//     check = arr.find(findNumber)
//     if (check){
//         return true
//     }return false
// }
// console.log(isExist());

//11
 // because sort works on string. which means that it sort in alphabet order. so in this case it will take the first character and it 
 // will check if it bigger than the other. for example 21 and 4, it will locate 21 before 4 because 2<4.

 //12
//  const numbers = [40, 100, 1, 5, 25, 10];
//  let newNumbers = numbers.sort(function(a, b){return a - b});
// console.log(newNumbers);    // i know that the function apply on the original array but for the next question i needed it inside variable
// this function check whether number a -b will give negative output. if it does, it means b is bigger than a. and so on..

//13
// let joinFunc = (numbers) =>{
//     return numbers.join("**")
// }

// console.log(joinFunc(newNumbers));

//14
// let strSort = (arr) =>{
//      return arr.sort();
// }
// const strArr = ['d','m','a'];
// console.log(strSort(strArr));

//15

// let isAllBelow = (arr, threshold) => {
//     return arr.every(value => value < threshold);
//   }
//   const numbers = [10, 15, 20, 25];
//   console.log(isAllBelow(numbers, 20)); 

//16
// function hasGreater(arr, number) {
//     return arr.some(value => value > number);
//   }
//   const numbers = [10, 15, 20, 20];
//   console.log(hasGreater(numbers, 20));
  
  