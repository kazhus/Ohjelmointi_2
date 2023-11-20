function doSomething(name) {
    console.log('Hello', + name);
}
const doSomething2 = function (name) {
    console.log('Greeting again', name);
} ;
const doSomething3 = (name) => {
    console.log('Greeting for third times', name)
};
doSomething( 'matti');
doSomething2('James');
doSomething3('Miro');
/*

function generateLotterryRow(numberCount, maxValue) {
    const lotteryRow = [];
    while (lotteryRow.length < numberCount) {
    const number = Math.floor(Math.random() * maxValue + 1);
    if (!lotteryRow.includes(number)) {
        lotteryRow.push(number);
    }

    console.log('arvotaan pallon arvo: ' + number);
}
return lotteryRow.sort((num1, num2) => num1-num2 );


const myRow = generateLotterryRow(7, 40);
console.log('myRow', myRow);
console.log(generateLotterryRow(9, 100));

function createLotteryTicket (rowCount) {
    const ticket = [];
for (let i = 0; i < rowCount, i++){
const row =generateLotterryRow(7, 40)}
ticket.push(row);
}
return ticket;
}
const myTicket = createLotteryTicket(5);
console.log('koko lottolappu', myTicket);
console.log(myTicket[1][2]);
*/