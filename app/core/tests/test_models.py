"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
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

    def test_create_user_test_result(self):
        """Test create a UserTestResult instance."""
        self.assertEqual(self.user_test_result.user, self.user)
        self.assertEqual(self.user_test_result.test_set, self.test_set)
        self.assertEqual(self.user_test_result.score, 80)
        self.assertEqual(self.user_test_result.total_questions, 10)
        self.assertEqual(self.user_test_result.total_questions, 10),
        self.assertEqual(self.user_test_result.correct_answers, 8)

    def test_percentage_calculation(self):
        """Test the percentage calculate method."""
        expected_percentage = (8 / 10) * 100
        self.assertEqual(self.user.percentage, expected_percentage)
