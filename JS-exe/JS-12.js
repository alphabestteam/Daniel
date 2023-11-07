//A
function Student(name, age, grades) {
  this.name = name;
  this.age = age;
  this.grades = grades;
  this.avg = average(grades, name);
}
average = (arr, name) => {
  let matches = name.match(/[aeiou]/gi);
  if (matches === null || matches.length === 0) {
    return arr.reduce((a, b) => a + b, 0) / arr.length;
  }
  return arr.reduce((a, b) => a + b, 0) / arr.length + matches.length;
};

const student1 = new Student("Chen", 32, [90, 89, 67, 89]);
const student2 = new Student("David", 32, [78, 98, 98, 90]);
const student3 = new Student("Ari", 32, [90, 90, 57, 67]);

const students = [student1, student2, student3];
for (const student of students) {
  console.log(students.indexOf(student));
  console.log(student);
}
//check if students over 18
const adults = students.filter((student) => student.age > 18);
console.log(adults);

//B
carAge = (year) => {
  currentYear = new Date();
  age = currentYear.getFullYear() - year;
  return age;
};

function Car(brand, model, year) {
  this.brand = brand;
  this.model = model;
  this.year = year;
  this.age = carAge(year);
}

let car1 = new Car("Citroen", "c4", 2011);
let car2 = new Car("Ford", "Explorer", 2013);
let car3 = new Car("Toyota", "prius", 2016);

cars = [car1, car2, car3];

for (const car of cars) {
  console.log(car);
}
