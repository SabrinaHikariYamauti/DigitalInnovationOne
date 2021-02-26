let line = gets().split(" "); // retorna  aproxima linha de entrada
let A = parseInt(line[0]);
let B = parseInt(line[1]);
let total = 0; // Altere o valor da variável com o cálculo esperado
console.log("X = " + total); //print na tela

let valor1 = parseInt(gets());//numero de um colaborador
let valor2 = parseInt(gets());//numero de horas trabalhadas
let valor3 = parseFloat(gets());//valor que recebe por hora
let salary = parseFloat(valor2 * valor3).toFixed(2); // Digite aqui o calculo do salário
console.log("NUMBER = " + valor1);
console.log("SALARY = U$ " + salary);