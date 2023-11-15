

    const nopat = parseInt(prompt('Kuinka monta noppaa halua heittää?'))

    let sum = 0;
    for (let i = 0; i < nopat; i++) {
        const number = Math.floor(Math.random() * 6 + 1) // se antaa meillä numero 1-6 välillä
        console.log(number)
        sum += number;
    }
    console.log(sum)
