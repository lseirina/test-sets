"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth.models import get_user_model
from core import models


class ModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Test Name',
            password='Test123',
        )
        self.test_set = models.TestSet.objects.create(
            title='Test Title',
            description='Test Text',
        )
        self.question = models.Question.objects.create(
            test_set=self.test_set,
            text='Test Text',
        )
        self.user_test_result = models.UserTestResult.objects.create(
            user=self.user,
            test_set=self.test_set,
            score=80,
            total_questions=10,
            correct_answers=8,
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
