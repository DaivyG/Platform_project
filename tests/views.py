from django.shortcuts import render, redirect
from .models import Question

def test_view(request):
    questions = Question.objects.all()  # Получаем все вопросы
    return render(request, 'tests/discipline_test.html', {'questions': questions})


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