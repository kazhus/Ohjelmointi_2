const numbers = [];
let input;
do {
    input = parseInt(prompt('Enter a number (enter 0 to stop): '));
    if (input !== 0 && !isNaN(input)) {
     numbers.push(input);
    }
} while (input !== 0);
numbers.sort((a, b) => b - a); //sort the number in descending order
console.log('Numbers in descending order :');
console.log(numbers);