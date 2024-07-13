<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

/**
 * The `ArticleController` class is responsible for handling requests related to articles.
 * It provides methods for creating, reading, updating, and deleting articles.
 */

class ArticleController extends Controller
{
    /**
     * Retrieves the index of the selected item.
     *
     * This method returns the index of the selected item in the collection.
     *
     * @return int The index of the selected item, or -1 if no item is selected.
     */
    public function fetchArticles()
    {
        $response = Http::get('http://article:8001/articles');
        return $response->json();
    }
}
