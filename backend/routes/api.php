<?php

use App\Http\Controllers\ApiController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/**
 * Route to get the authenticated user.
 *
 * This route returns the authenticated user's information.
 * It uses the 'auth:sanctum' middleware to ensure that the request is authenticated.
 *
 * @param \Illuminate\Http\Request $request
 * @return \Illuminate\Http\JsonResponse
 */
Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

/**
 * Route to get articles.
 *
 * This route calls the getArticles method of the ApiController to fetch articles
 * from an external FastAPI endpoint and return them in JSON format.
 *
 * @return \Illuminate\Http\JsonResponse
 */
Route::get('/api/articles', [ApiController::class, 'getArticles']);

/**
 * Route to get photos.
 *
 * This route calls the getPhotos method of the ApiController to fetch photos
 * from an external FastAPI endpoint and return them in JSON format.
 *
 * @return \Illuminate\Http\JsonResponse
 */
Route::get('/api/photos', [ApiController::class, 'getPhotos']);
