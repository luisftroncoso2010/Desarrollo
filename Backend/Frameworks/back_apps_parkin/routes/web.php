<?php

use App\Http\Controllers\LoginsController;
use Illuminate\Support\Facades\Route;





Route::get('/', [LoginsController::class,'index'])->name('Logind.index');