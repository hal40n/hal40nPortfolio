<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;

/**
 * ApiController
 *
 * This controller is responsible for fetching articles and photos from external FastAPI endpoints.
 * It uses Guzzle HTTP client to send GET requests and return the responses in JSON format.
 */
class ApiController extends Controller
{
    protected $client;

    /**
     * Constructor
     *
     * Initializes the Guzzle HTTP client.
     */
    public function __construct()
    {
        $this->client = new Client();
    }

    /**
     * Get Articles
     *
     * Fetches articles from the FastAPI endpoint specified in the environment variable.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function getArticles()
    {
        $url = env('FASTAPI_ARTICLES_URL');

        $articles = $this->getJson($url);
        return $articles;
    }

    /**
     * Get Photos
     *
     * Fetches photos from the FastAPI endpoint specified in the environment variable.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function getPhotos()
    {
        $url = env('FASTAPI_PHOTOS_URL');

        dd($url);
        $photos = $this->getJson($url);
        return $photos;
    }

    /**
     * Get JSON
     *
     * Sends a GET request to the specified URL and returns the response in JSON format.
     *
     * @param string $url
     * @return \Illuminate\Http\JsonResponse
     */
    function getJson($url)
    {
        try {
            $response = $this->client->request('GET', $url);
            $result = json_decode($response->getBody(), true);

            return response()->json($result);
        } catch (RequestException $e) {
            return response()->json(['error' => 'An error occurred while fetching data'], 500);
        }
    }
}