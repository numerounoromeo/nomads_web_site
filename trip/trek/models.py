from django.db import models

class Trek(models.Model):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    DIFFICULTY_LEVEL_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    difficulty_level = models.CharField(max_length=1,choices=DIFFICULTY_LEVEL_CHOICES)
	trek_name = models.CharField(max_length=150)
	duration = models.DurationField()
	overview = models.TextField()
	location = models.ForeignKey(Location,on_delete=models.CASCADE)	
	
	def __str__(self):
		return self.trek_name
		
		
class Location(models.Model):
	state = models.CharField(max_length=150)
	district = models.CharField(max_length=150)
    
	def __str__(self):
		return self.state +'/'+ self.district