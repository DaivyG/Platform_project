from django.shortcuts import render
from django.shortcuts import redirect

def main(request):
    return render(request, 'main/main_page.html')

def university_list(request):
    # Здесь можете получить список университетов из базы данных или другого источника данных
    universities = [
        {'id': 1, 'name': 'СПБПУ'},
        # Добавьте здесь другие университеты, если есть
    ]
    return render(request, 'main/university_list.html', {'universities': universities})

def discipline_list(request, university_id):
    # Здесь можете получить список дисциплин для данного университета из базы данных или другого источника данных
    # Например, для университета с ID = university_id
    disciplines = [
        {'id': 1, 'name': 'Дисциплина 1'},
        {'id': 2, 'name': 'Дисциплина 2'},
        # Добавьте здесь другие дисциплины, если есть
    ]
    return render(request, 'main/discipline_list.html', {'disciplines': disciplines})

def start(request):
    # Обработка нажатия на кнопку "Начать": перенаправляем пользователя на страницу списка университетов
    return redirect('university_list')