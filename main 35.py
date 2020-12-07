def favorite_genres(users, movies, movie_ratings):
  user_dict = {}
  movie_dict = {}
  for user in users:
    user_id = user["id"]
    user_dict[user_id] = {} # dict of genre keys with (sum_total_score, num_scores) array
  for movie in movies:
    movie_id = movie["id"]
    movie_genre = movie["genre"]
    movie_dict[movie_id] = movie_genre
  for movie_rating in movie_ratings:
    user_id = movie_rating["user_id"]
    movie_id = movie_rating["movie_id"]
    rating = movie_rating["rating"]
    genre = movie_dict[movie_id]
    if genre not in user_dict[user_id]:
      user_dict[user_id][genre] = [rating,1]
    else:
      user_dict[user_id][genre][0] += rating
      user_dict[user_id][genre][1] += 1
  
  users = []
  for user_id,value in user_dict.items():
    new_JSON_entry = {}
    new_JSON_entry["id"] = user_id
    fav_genre = ""
    high_score = float("-inf")
    for genre,info in value.items():
      sum_total_score, num_scores = info
      score = sum_total_score/num_scores
      if score > high_score:
        high_score = score
        fav_genre = genre
    new_JSON_entry["favorite_genre"] = fav_genre
    users.append(new_JSON_entry)
    
  return users
      
    
    