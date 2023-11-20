const dogNames = [];
for (let i = 0; i <6; i ++){
    let name = prompt('Enter dog name ' + (i + 1) + ':');
    dogNames.push(name);
}
dogNames.sort(); //sorting names of the dog
dogNames.reverse(); //reverse the sorted

document.write('<ul>'); //start unorder list
for (let i = 0; i < dogNames.length; i++){
    document.write('<li>' + dogNames [i] + '</li>'); //print each name as a list item
}
    document.write ('</ul>'); //End unorder list