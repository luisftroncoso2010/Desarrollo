let expr = 'Uvas'

switch (expr) {
    case 'Naranjas':
        console.log('Las naranjas cuestan $20 pesos el kilo');
        break;
    case 'Manzanas':
        console.log('Las manzanas cuestan $43 el kilo');
        break;
    case 'Plátanos':
        console.log("El plátamps esta en $30 el kilo");
        break;
    case 'Mangos':
    case 'Papayas':
        console.log('Los mangos y las papayas cuentas $25');       
    default:
        console.log('Lo siento no encontramos tu producto');        
}
console.log('¿Algo más que desees?');
