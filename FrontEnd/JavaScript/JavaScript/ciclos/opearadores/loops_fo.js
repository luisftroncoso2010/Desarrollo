console.log("   * Loop: for");

let list = ['eat', 'sleep', 'code', 'repeat']

for (let index = 0; index < list.length; index++) {
    console.log(list[index]);
}

console.log("   * Loop: for of");

for (const element of list) {
    console.log(element);   
}