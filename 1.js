// Массив заполняется змейкой

const maxValue = 5;
const defaultNumber = 10;

let array = [];
let number = defaultNumber;

for (let i = 0; i < maxValue; i ++){
	array.push([...generateSequence(maxValue)]);
}

function* generateSequence(end) {
	for (let i = 0; i < end; i++) yield 0;
}

function vector(){
	this.begin = 0;
	this.end = maxValue - 1;
}

let vertical = new vector();
let horizontal = new vector();

while(true){
	if (number == defaultNumber + maxValue ** 2){
		break;
	}
	for (let x = vertical.begin; x <= vertical.end; x ++){
		array[x][horizontal.begin] = number ++;
	}
	horizontal.begin ++;
	
	for (let x = horizontal.begin; x <= horizontal.end; x ++){
		array[vertical.end][x] = number ++;
	}
	vertical.end --;
	
	for (let x = vertical.end; x >= vertical.begin; x --){
		array[x][horizontal.end] = number ++;
	}
	horizontal.end --;

	for (let x = horizontal.end; x >= horizontal.begin; x --){
		array[vertical.begin][x] = number ++;
	}
	vertical.begin ++;
}

for (row of array){
	console.log(row);
}
