// Variable local
const userPoint = 150

function checkAccess(){
    if(userPoint < 100){
        const message = "Access denied: Insufficient points!"
        return message
    } else {
        const message = "Accees granted: Enjoy the premium features!"
        return message
    }
}

console.log(checkAccess());

