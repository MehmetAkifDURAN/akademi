from django.shortcuts import render
from academyapp.models import CategoryLevelOne, CategoryLevelTwo, Course
from json import dumps

# Create your views here.


def convertToJson(categories):
    return dumps({'categories': categories})


def getCategories(categories, level=1):
    _categories = []
    for category in categories:
        _categories.append(
            {
                'id': category.id,
                'name': category.category_name,
                'sub_categories': getCategories(category.sub_categories.all().order_by('order_number'), level=level+1) if type(category) != CategoryLevelTwo else None,
                'level': level,
                'slug': category.slug
            }
        )
    return _categories


def index(request):
    context = {
        'categories_level_one': convertToJson(getCategories(CategoryLevelOne.objects.all().order_by('order_number'))),
        'courses': Course.objects.filter(is_active=True)
    }
    return render(request, 'academyapp/index.html', context)


def getCoursesByCategory(request, slug_category):
    context = {
        'categories_level_one': convertToJson(getCategories(CategoryLevelOne.objects.all().order_by('order_number')))
    }

    courses = []
    if CategoryLevelOne.objects.filter(slug=slug_category).exists():
        category = CategoryLevelOne.objects.get(slug=slug_category)
        for sub_category in category.sub_categories.all():
            courses = courses + [course for course in Course.objects.filter(
                is_active=True, category_level_two=sub_category)]
    elif CategoryLevelTwo.objects.filter(slug=slug_category).exists():
        category = CategoryLevelTwo.objects.get(slug=slug_category)
        courses = Course.objects.filter(
            is_active=True, category_level_two=category)
    else:
        return render(request, 'errors/404.html', context)

    context['category'] = category
    context['courses'] = courses
    return render(request, 'academyapp/course-list.html', context)
