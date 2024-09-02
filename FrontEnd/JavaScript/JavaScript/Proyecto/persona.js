const usersDatabase=[
    {username:"andres", password:"123"},
    {username:"caro",password:"456"},
    {username:"mariana",password:"789"},
    {username: "oscar", password: "123"}
];

const usersTimeline=[
    {username:"Caro", timeline:"Me encata Javascript!",},
    {username:"Oscar", timeline:"Bebeloper es lo mejor!"},
    {username:"Mariana", timeline:"A mi me gusta mÃ¡s el cafÃ© que el tÃ©"},
    {username:"Andres", timeline:"Yo hoy no quiero trabajar"}
];

let nombre = prompt('* Digite userName: ')
let contrasena = prompt('* Coloque su Password: ')
let usuarioEncontrado = false

for (let element = 0; element < usersDatabase.length; element++) {
    if (nombre == usersDatabase[element].username  && contrasena == usersDatabase[element].password) {
        usuarioEncontrado = true

        for (let user of usersTimeline) {   
            let userMayucula = usersDatabase[element].username.charAt(0).toUpperCase()
            let residuoString = usersDatabase[element].username.slice(1)
            const nombreMayuscula = userMayucula + residuoString        
            
            if(nombreMayuscula == user.username){
                alert(`OK. User Name: ${user.username}. Time Line: ${user.timeline}`) 
                break               
            }                                        
        }         
    }
}

if(!usuarioEncontrado) alert("Valide su usuario o contraseña por favor")

