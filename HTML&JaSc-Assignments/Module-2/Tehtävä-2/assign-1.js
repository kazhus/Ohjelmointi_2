const numbParticipants = parseInt(prompt('Enter number of participants: '));
const participantsNames = [];
for (let i = 0; i <numbParticipants; i++){
    let name = prompt('Enter participants names: ' + (i + 1) + ':');
    participantsNames.push(name);
}
participantsNames.sort();
document.write('<ol>'); //starts order list
for (let i = 0; i <participantsNames.length; i ++) {
    document.write('<li>' + participantsNames [i] + '</li>'); //print each name as a list item
}
document.write('</ol>'); //order list ended