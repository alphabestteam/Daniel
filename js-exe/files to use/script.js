const main = document.querySelector('main');



function headingFactory(color){    
    function createHeading(text){
        const heading = document.createElement('h1');
        heading.setAttribute('style', 'color: ' + color);
        heading.textContent = text;
        return heading;
}
return createHeading;
}

// red and blue holding headingFactory's return value. 
//and because the return value is a function|(Closures)|, we can use "red" or "blue" as the inner function and define the text

const red = headingFactory("red");
const blue = headingFactory("blue") ;

const factory1 = red("using factory 1");
const factory2 = blue("using factory 2");
const factory3 = red("using factory3");

main.appendChild(factory1);
main.appendChild(factory2);
main.appendChild(factory3)



//3. They provide simplicity to the code, allowing the programmer and any other party to understand the code at a high level easily