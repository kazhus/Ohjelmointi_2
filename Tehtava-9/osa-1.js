const joukujuttu = 'Hello' ;
const items = ['eka', 2, 2.3, [1, 2, 3], true, joukujuttu];
console.log(items);
console.log(items[3]);
items[3] = 999;
console.log(items[3]);

items[9] = '10. alkion esimerkkiarvo';
console.log(items);
console.log(items[6]);

console.log(items.length);

console.log('Tulostesaann kaikkieln alkoididen arcor for;lla')
for (let i=0; i<items.length; i++) {
    console.log(i + '.alkoion arvo on ' + items[i]);
}
for (const item of items) {
    if (item) {
    console.log(item);
    }
}
//Taloukioden methodi
const names = ['Anni', 'James', ' Scoot', 'Katrin'];
const age = [52, 24, 30, 28];
console.log(names);

items.sort();
console.log(names);
console.log(age);
age.sort((a, b) => a-b)
console.log(age);


age.reverse();
console.log(age);
//add new names/items
names.push('Suvi');
console.log(names);
names.unshift('Alexi');
console.log(names);
//remove or reserve it last items
names.pop();
console.log(names);

const lastNameInArr = names.pop();
console.log('taulostaan poistetaann', lastNameInArr);
console.log(names);

names.includes('James');
console.log(names.includes('James'));
console.log(names.includes('Ali'));
//adding items and check it out if it is in the list
names.push('Ali');
console.log(names.includes('Ali'));

//java script object
const person = {name: "Viola", age: 29, profession: 'ICT assistant'};
console.log('person-olio', person);

//reorder properties of items
person['age'] = 30;
person.name ='Saeid';
person.profession = 'student';
console.log('person-päivitetty', person);
console.log(person.name + 'on' + person.age + 'vuotias.');

//creating function

const person2 = {
    name: 'Javad',
    age : 66,
    getInfo: function () {
        return this.name + ' on ' + this.age + ' -vuotias' ;
    }
}
person2.getInfo()
console.log(person2.getInfo());
