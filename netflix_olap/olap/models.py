from django.db import models

# most popular shows
class PopShow(models.Model):
    user_id = models.IntegerField()
    show_id = models.IntegerField()
    show_name = models.CharField(max_length = 255)
    ratings_id = models.IntegerField()

# most popular movies
class PopMovie(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length = 255)
    ratings_id = models.IntegerField()

# most popular genre
class PopGenre(models.Model):
    user_id = models.IntegerField()
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length = 255)
    ratings_id = models.IntegerField()

# most preferred plan
class PopPlan(models.Model):
    user_id = models.IntegerField()
    plan_id = models.IntegerField()
    plan_name = models.CharField(max_length = 255)

# most active users
class ActiveUser(models.Model):
    user_id = models.IntegerField()
    watched_num = models.IntegerField()
