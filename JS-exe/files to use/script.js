function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA();
// questionB();
// questionC();
// questionD();
questionE();

//I will explain the concept and the different of macro task vs micro task and than i'll go through all the questions.
// Macro task - High-level asynchronous operations like setTimeout, setInterval, I/O operations, and UI rendering.
// the tasks is executed by the event loop that works in fifo order.It execute when call stack have lower priority compared to Micro task

// Micro task - Low-level asynchronous operations such as promises.
// Executed immediately after the call stack is empty.
// Have higher priority than macro tasks and are typically used for high-priority asynchronous work.

//question A - the setTimeout = 0. first it get into the event loop, continue to the log and execute it. console.log is Micro task.
//question B - promise will execute first, and than the Timeout. promise its micro task and get more priority than time out which is Macro task
//question C - The order is Promise at C first (synchronous), and  Timeout at C second (as a macro task, delayed by 1000 milliseconds).
//question D - first the log(sponge) execute immediately, then,the timeOut get into the eventLoop next the promise get into the eventloop, then the 
//             log(bob) execute, now it back to the event loop and get from there the promise because it micro task and then the time out
//question E - First, it get into the first function, and get the promise into event loop, and then the time out. Enter the second function, 
// get the promise and the time out to the event loop. 1. execute the first promise 2. execute the second.,then the first time out and then the second time out
