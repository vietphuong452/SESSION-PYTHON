var movie = {
    Title:"Spider-Man",
    Rating:"10",
}

movie.Rating = 9;
console.log(movie["Rating"]);
var prop = "Rating"
console.log(movie[prop]);
movie["Year"]= 2014
console.log(movie)