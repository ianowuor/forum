from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=256)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.question}'
    
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField()
    upvotes = models.IntegerField(default=0, null=True)
    downvotes = models.IntegerField(default=0, null=True)

    def __str__(self) -> str:
        return f'{self.comment}'
    
    def increase_upvotes(self):
        self.upvotes += 1
        self.save()

    def decrease_upvotes(self):
        if self.upvotes > 0:
            self.upvotes -= 1
            self.save()

    def increase_downvotes(self):
        self.downvotes += 1
        self.save()

    def decrease_downvotes(self):
        if self.downvotes > 0:
            self.downvotes -= 1
            self.save()