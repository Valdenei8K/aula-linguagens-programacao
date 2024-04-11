const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Digite um número: ', (input) => {
    const idade = parseInt(input);

    if (idade<= 12) {
        console.log('criança');
    }
    else if (idade <=18){
        console.log('adolescente');
    }
    else if (idade <=60){
        console.log('adulto')
    }

     else {
        console.log('idoso');
    }

    readline.close();
})