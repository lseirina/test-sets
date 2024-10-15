"""
Models for db.
"""

from django.db import models
from django.contrib.auth.models import User


class TestSet(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test_set = models.ForeignKey(
        TestSet, on_delete=models.CASCADE, related_name='question'
        )
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer', default=1
        )
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    correct_answers = models.IntegerField()

    def persentage(self):
        return (self.correct_answers / self.total_questions) * 100
