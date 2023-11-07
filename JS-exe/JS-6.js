function evalNumbers(num1, num2, operation) {
  let result;
  switch (operation) {
    case "+":
      result = num1 + num2;
      console.log(`The result of addition is: ${result}`);
      break;
    case "-":
      result = num1 - num2;
      console.log(`The result of subtraction is: ${result}`);
      break;
    default:
      console.log("Invalid operation");
  }
}

evalNumbers(5, 3, "+");
evalNumbers(10, 8, "-");
