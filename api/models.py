from django.db import models
import string
import random


def generate_unique_codes():
    length = 6
    while True:
        #creates code that makes a code that is k length and uppercase ascii
        code = ''.join(random.choices(string.ascii_uppercase), k=length)
        if Room.objects.filter(code=code).count() == 0:
            break

    return code



# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default ="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False) #if null is false, it has to be filled out
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True) #adds the time that it was created at
   
    

