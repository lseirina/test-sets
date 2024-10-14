"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from core import models


class ModelTests(TestCase):

    def setUp(self):
        self.test_set = models.TestSet.objects.create(
            title='Test Title',
            text='Test Text',
        )
        self.question = models.Question.objects.create(
            test_set=self.test_set,
            text='Test Text',
        )

    def test_create_test_set(self):
        test_set = models.TestSet.objects.create(
            title='Another Test Title',
            description='Another Test text',
        )

        self.assertEqual(test_set.title, str(test_set))

    def test_create_question(self):
        question = models.Question.objects.create(
            test_set=self.test_set,
            text='Test Text',
        )

        self.assertEqual(question.text, str(question))

    def test_create_answer(self):
        answer = models.Answer.objects.create(
            question=self.question,
            text='Test Text',
        )

        self.assertEqual(answer.text, str(answer))
