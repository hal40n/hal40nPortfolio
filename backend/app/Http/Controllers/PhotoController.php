<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;


/**
 * Class PhotoController
 *
 * This class is responsible for handling photo-related operations.
 */
class PhotoController extends Controller
{
    /**
     * Fetches photos from the photo service.
     *
     * @return array The JSON response from the photo service.
     */
    public function fetchPhotos()
    {
        $response = Http::get('http://photo:8001/photos');
        return $response->json();
    }
}