dineroCofla = prompt('¿Cuanto dinero tiene Cofla?');
dineroRoberto = prompt('¿Cuanto dinero tienes roberto?');
dineroPedro = prompt('¿Cuanto dinero tiene Pedro ?');

if (dineroCofla > 0.6 && dineroCofla < 1){
    alert('comprate el helado de agua')
}
else if (dineroCofla >= 1 && dineroCofla < 1.6){
    alert('comprate el helado de crema') 
}
else if (dineroCofla >= 1.6 && dineroCofla < 1.7){
    alert('comprate el helado de heladix') 
}
else if (dineroCofla >= 1.7 && dineroCofla < 1.8){
    alert('comprate el helado de heladovich') 
}
else if (dineroCofla >= 1.8 && dineroCofla < 2.9){
    alert('comprate el helado de helardo') 
}
else if (dineroCofla >= 2.9 ){
    alert('Holado con confites o el pote de 1/4kg') 
} else {
    alert('Lo siento no te alcanza para ningun helado')
}
    


