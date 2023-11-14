'use strict'
const print_name = document.querySelector('#print_name');
const name= prompt('Please give your name:');
console.log(name);
print_name.innerHTML = `Hello, ${name}!`;
