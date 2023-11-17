from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'snake_salad': {
        'майонез, г': 30,
        'оливки, шт': 2,
    }
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Омлет': 'omlet/?servings=1',
        'Паста': 'pasta/?servings=1',
        'Бутерброд': 'buter/?servings=1',
        'Салат Змейка': 'snake_salad/?servings=1'
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def recipes(request, recipe):
    servings = int(request.GET.get('servings', 1))
    ingredients = {ingr: value * servings for ingr, value in DATA.get(recipe, {}).items()}
    return render(request, 'calculator/index.html', {'recipe': ingredients})