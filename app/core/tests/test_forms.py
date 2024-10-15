"""Tests for froms"""

from django import TestCase
from core.models import TestSet, Question, Answer
from core.forms import QuestionForm


class QuestionFormTest(TestCase):

    def setUp(self):
        self.test_set = TestSet.objects.create(
            title='Test Title',
            text='Sample Text',
        )
        self.question = Question.objects.create(
            test_set=self.test_set,
            description='Sample Description',
        )
        self.answer1 = Answer.objects.create(
            question=self.question,
            text='Answer1',
        )
        self.answer2 = Answer.objects.create(
            question=self.question,
            text='Answer2',
        )
        self.answer3 = Answer.objects.create(
            question=self.question,
            text='Answer3'
        )
