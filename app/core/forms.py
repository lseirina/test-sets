from django import forms
from core.models import Answer


class QuestionForm(forms.Form):
    answers = forms.ModelMultipleChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.CheckBoxSelectMultiple,
        required=True
    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.all()
