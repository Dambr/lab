// Вывод простых чисел до N

let N = 10;
let count = 0;

function isPresent(x){
	let max = Math.sqrt(x);
	for (let i = 2; i <= max; i ++){
		if (x % i == 0){
			return false;
		}
	}
	return true;
}

function nextPresent(x){
	let step = 1;
	while(true){
		if ( isPresent(x + step) ){
			return x + step;
		}
		step ++;
	}
}

let number = nextPresent(1);

while(number < N){
	console.log(number);
	number = nextPresent(number);
}
