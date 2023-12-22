import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course, Student


# Фикстура для APIClient
@pytest.fixture
def client():
    return APIClient()


# Фикстура для фабрики курсов
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Фикстура для фабрики студентов
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# Test Scenario 1: Проверка получения первого курса
@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/1/')

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course[0].name


# Test Scenario 2: Проверка получения списка курсов
@pytest.mark.django_db
def test_get_course_list(client, course_factory):
    course = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
    for i, m in enumerate(data):
        assert m['name'] == course[i].name


# Test Scenario 3: Проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_course_by_id(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f'/api/v1/courses/?id={course[0].id}')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
    assert data[0]['id'] == course[0].id


# Test Scenario 4: Проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_course_name(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f'/api/v1/courses/?name={course[0].name}')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(course)
    assert data[0]['name'] == course[0].name


# Test Scenario 5: Тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'Django Test with Pytest'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# Test Scenario 6: Тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)

    request_patch = client.patch(f'/api/v1/courses/{course[0].pk}/', data={'name': 'Django Test with Pytest'})
    data_request_patch = request_patch.json()
    response = client.get(f'/api/v1/courses/{course[0].pk}/')
    data_response = response.json()

    assert request_patch.status_code == 200
    assert response.status_code == 200
    assert data_request_patch['name'] == data_response['name']


# Test Scenario 7: Тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    count = Course.objects.count()

    del_request = client.delete(f'/api/v1/courses/{course[0].pk}/')
    get_request = client.get(f'/api/v1/courses/{course[0].pk}/')

    assert del_request.status_code == 204
    assert get_request.status_code == 404
    assert Course.objects.count() == count - 1
