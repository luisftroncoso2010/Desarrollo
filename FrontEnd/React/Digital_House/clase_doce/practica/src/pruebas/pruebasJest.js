import pkg from '@jest/globals';
const { expect, test, describe } = pkg;

const sum = (a, b) => a + b;

test('should  sum two numbers', () => {
    const numberUno = 2;
    const numberDos = 3;

    const resulta = sum(numberUno, numberDos)
    expect(resulta).toBe(5)
  
})
