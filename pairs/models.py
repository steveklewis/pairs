
from django.db import models


class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.word

    def __str__(self):
        return self.word

    
class Emotion(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    tags = models.ManyToManyField(Tag, related_name="emotions")

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.family)

    def __str__(self):
        return "%s (%s)" % (self.name, self.family)

    


class EmotionPair(models.Model):
    left = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name="left")
    right = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name="right")
    name = models.CharField(max_length=200)
    
    tags = models.ManyToManyField(Tag, related_name="pairs")


    def __str__(self):
        return "%s (%s <-> %s)" % (self.name, self.left.name, self.right.name)


