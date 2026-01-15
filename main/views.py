from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def video_gallery(request):
    # Список відео. Можете замінити ID (те, що після embed/) на свої з YouTube
    videos = [
       {'title': 'Що таке Supply Chain Management', 'youtube_id': 'Lpp9bHtPAN0'},
        
        # 2. Wendover Productions: Як працює доставка за ніч (Авіа) - дуже популярне
        {'title': 'Логістика нічної доставки (Авіа)', 'youtube_id': 'y3qfeoqErtY'},
        
        # 3. Brightpick: Найсучасніший роботизований склад
        {'title': 'Роботи на складі (AI Automation)', 'youtube_id': 'U2AGLeJBFNg'},
    ]
    return render(request, 'videos.html', {'videos': videos})