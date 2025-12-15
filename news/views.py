from django.shortcuts import render
from django.http import JsonResponse  # ЧАТБОТ
from django.db.models import Q        # ЧАТБОТ
import re                             # ЧАТБОТ
from main.models import News  

def news_list(request):
    news = News.objects.order_by('-date')
    return render(request, 'news.html', {'news': news})
# --- ЧАТБОТ ---
def chat_search(request):
    # Отримуємо текст, який ввів користувач
    q = request.GET.get('q', '').strip()
    data = []

    if q:
        # Перетворюємо в нижній регістр і розбиваємо на окремі слова
        normalized = q.lower()
        tokens = re.findall(r'\w+', normalized, flags=re.U)
        
        search_q = Q()
        for t in tokens:
            # Пропускаємо надто короткі слова (менше 2 літер)
            if len(t) < 2:
                continue
            # Шукаємо це слово або в заголовку, або в тексті новини
            search_q |= Q(title__icontains=t) | Q(content__icontains=t)
            
        # Якщо знайшли якісь слова для пошуку
        if search_q:
            # Шукаємо в базі, беремо тільки 5 найсвіжіших результатів
            qs = News.objects.filter(search_q).order_by('-date')[:5]
            
            # Перетворюємо новини у список даних для відповіді
            for item in qs:
                data.append({
                    'title': item.title,
                    'date': item.date.strftime('%Y-%m-%d'),
                    'id': item.id
                })

    # Повертаємо результат у форматі JSON (для чат-бота)
    return JsonResponse({'results': data})