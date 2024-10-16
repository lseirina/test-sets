"""Views for test sets"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import TestSet, Question, UserTestResult
from core.forms import QuestionForm


@login_required
def start_test(request, test_set_id):
    test_set = get_object_or_404(TestSet, id=test_set_id)
    questions = test_set.questions.all()
    if 'current_question' not in request.session:
        request.session['current_question'] = 0
        request.session['score'] = 0

    current_question = questions[request.session['current_question']]
    if request.method == 'POST':
        form = QuestionForm(current_question, request.POST)
        if form.is_valid():
            selected_answers = form.cleaned_data['answers']
            if all(answer.is_correct for answer in selected_answers) and \
               len(selected_answers) == current_question.answer.filter(
                   is_correct=True
                   ).count():
                request.session['score'] += 1
            request.session['current_question'] += 1
            if request.session['current_question'] < len(questions):
                return redirect('start_test', test_set_id=test_set.id)
            else:
                return redirect('test_result', test_set_id=test_set.id)
    else:
        form = QuestionForm(current_question)

    return render(
        request, 'test.html', {'question': current_question, 'form': form}
        )
