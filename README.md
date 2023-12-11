# Move Rating MapReduce
This repository calculates the average rating for each movie in a JSON file, following the Map-Reduce paradigm.

## Example

```json
[{"user_id":1,"movie_id":10,"rating":3},
{"user_id":2,"movie_id":1,"rating":5},
{"user_id":3,"movie_id":9,"rating":5},
{"user_id":4,"movie_id":9,"rating":2},
{"user_id":5,"movie_id":10,"rating":3},
{"user_id":6,"movie_id":7,"rating":5},
{"user_id":7,"movie_id":8,"rating":2},
{"user_id":8,"movie_id":10,"rating":5},
{"user_id":9,"movie_id":7,"rating":1},
{"user_id":10,"movie_id":1,"rating":1}]
```
Using the JSON file above, it will calculate the average rating with the Map-Reduce paradigm and return:
```doctest
[('movie_id 1', 3.0), ('movie_id 7', 3.0), ('movie_id 8', 2.0), ('movie_id 9', 3.5), ('movie_id 10', 3.67)]
```