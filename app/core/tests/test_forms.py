"""Tests for froms"""

from django.test import TestCase
from core.models import TestSet, Question, Answer
from core.forms import QuestionForm


class QuestionFormTest(TestCase):

    def setUp(self):
        self.test_set = TestSet.objects.create(
            title='Test Title',
            description='Sample Text',
        )
        self.question = Question.objects.create(
            test_set=self.test_set,
            text='Sample Description',
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

    def test_form_initialization(self):
        """Test form initializate correctly."""
        form = QuestionForm(question=self.question)

        self.assertQuerysetEqual(
            form.fields['answer'].queryset,
            Answer.objects.filter(question=self.question),
            transform=lambda x: x.id
        )

    def test_valid_form_submission(self):
        """Test valid Post data."""
        data_form = {
            'answers': [self.answer1.id, self.answer2.id]
        }
        form = QuestionForm(self.question, data_form)

        self.assertTrue(form.is_valid())

    def test_invalid_form_submission(self):
        """Test invalid POST data."""
        data_form = {}
        form = QuestionForm(self.question, data_form)

        self.assertFalse(form.is_valid())
