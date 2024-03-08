import json
from .models import Question, Answer

def load_questions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for question_text, answers_data in data.items():
            question = Question.objects.create(text=question_text)
            for answer_text in answers_data[0]:
                is_correct = answer_text in answers_data[1]
                Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)
                