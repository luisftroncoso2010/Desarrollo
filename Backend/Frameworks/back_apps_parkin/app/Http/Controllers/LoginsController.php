<?php

namespace App\Http\Controllers;

use App\Models\Logins;
use Illuminate\Http\Request;

class LoginsController extends Controller
{
    
    public function index() // Pagina de inicio del crud
    {
        
    }
        public function create() // formulario
    {
        //
    }

   
    public function store(Request $request) // Guarda datos en la BDD
        {
        //
    }

   
    public function show(Logins $logins) // Optiene un registro de la tabla
    {
        //
    }

    
    public function edit(Logins $logins) // Trae los datos que se van a editar y se colocan en un formulario
    {
        //
    }

   
    public function update(Request $request, Logins $logins)
    { // Actualiza los datos en la BD
        //
    }
    
    public function destroy(Logins $logins)
    {
        // Elimina un registro
    }
}
