from django.shortcuts import render
from .models import Question, Answer, TestResult
from django.shortcuts import redirect

def test_view(request):
    questions = Question.objects.all()  # Получаем все вопросы
    return render(request, 'tests/discipline_test.html', {'questions': questions})


def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        chosen_answer_id = request.POST.get('chosen_answer_id')
        question = Question.objects.get(pk=question_id)
        chosen_answer = Answer.objects.get(pk=chosen_answer_id)
        is_correct = chosen_answer.is_correct
        # Сохраняем результат теста
        TestResult.objects.create(user=request.user, question=question, chosen_answer=chosen_answer, is_correct=is_correct)
        # Возвращаем результат
        return render(request, 'tests/submit_answer.html', {'is_correct': is_correct})


def check_answer(request):
    if request.method == 'POST':
        # Получаем данные, отправленные пользователем
        selected_answers = request.POST.getlist('answer')  # Предполагается, что имя чекбоксов в HTML - 'answer'

        # Получаем id вопросов, на которые пользователь отвечал
        question_ids = [int(question_id) for question_id in selected_answers]

        # Получаем объекты вопросов из базы данных
        questions = Question.objects.filter(id__in=question_ids)

        # Создаем словарь, в котором ключи - это объекты вопросов, а значения - ответы пользователя
        user_answers = {}
        for question in questions:
            user_answers[question] = request.POST.getlist(str(question.id))  # Предполагается, что имя чекбоксов в HTML - id вопроса

        # Проверяем ответы пользователя и сравниваем их с правильными ответами
        results = {}
        for question, user_answer in user_answers.items():
            correct_answers = [answer.text for answer in question.answer_set.filter(is_correct=True)]
            results[question] = all(answer in correct_answers for answer in user_answer)

        # Отображаем результаты проверки
        return render(request, 'tests/result.html', {'results': results})

    else:
        # Если метод запроса не POST, перенаправляем пользователя обратно на страницу теста
        return redirect('test')  # Предполагается, что имя URL-шаблона для страницы теста - 'test'