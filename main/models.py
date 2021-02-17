from django.db import models


# Create your models here.
class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    rawg_id = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    age_rating_id = models.IntegerField()
    sys_req = models.TextField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Games'
        managed = False
        db_table = 'games'

#     CREATE TABLE entitys.games (
#     id integer NOT NULL,
#     rawg_id integer,
#     title text NOT NULL,
#     description text,
#     release_date date,
#     age_rating_id integer,
#     sys_req text
# );
