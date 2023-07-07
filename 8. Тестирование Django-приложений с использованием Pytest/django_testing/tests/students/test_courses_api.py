import random
import pytest
from students.models import Student, Course
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Проверка получения курса
@pytest.mark.django_db
def test_first_course_check(client, student_factory, course_factory):
    students = student_factory(_quantity=10)
    students_id = [i.id for i in students]
    courses = course_factory(_quantity=10, students=students)
    response = client.get(f"/courses/{courses[6].id}/")
    assert response.status_code == 200
    assert response.data["id"] == courses[6].id
    assert response.data["name"] == courses[6].name
    assert response.data["students"][5] == students_id[5]


# Проверка получения списка курсов
@pytest.mark.django_db
def test_course_list_check(client, student_factory, course_factory):
    students = student_factory(_quantity=10)
    students_id = [i.id for i in students]
    courses = course_factory(_quantity=10, students=students)
    response = client.get(f"/courses/")
    assert response.status_code == 200
    assert len(response.json()) == 10
    for i, c in enumerate(courses):
        assert response.data[i]["id"] == c.id
        assert response.data[i]["name"] == c.name
        assert response.data[i]["students"] == students_id


# Проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_checking_course_list_filtering_for_id(client, course_factory):
    courses = course_factory(_quantity=10)
    random_course = random.choice(courses)
    response = client.get(f"/courses/?id={random_course.id}")
    assert response.status_code == 200
    assert response.data[0]["id"] == random_course.id


# Проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_checking_course_list_filtering_for_name(client, course_factory):
    courses = course_factory(_quantity=10)
    random_course = random.choice(courses)
    response = client.get(f"/courses/?name={random_course.name}")
    assert response.status_code == 200
    assert response.data[0]["name"] == random_course.name


# Тест успешного создания курса
@pytest.mark.django_db
def test_successful_course_creation(client):
    data = {"name": "test"}
    response = client.post("/courses/", data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "test"


# Тест успешного обновления курса
@pytest.mark.django_db
def test_a_successful_course_update(client, course_factory):
    courses = course_factory(_quantity=10)
    update_name = "Lol_Kek_Cheburek"
    response = client.patch(
        f"/courses/{courses[6].id}/", data={"name": update_name}, format="json"
    )
    assert response.status_code == 200
    assert response.data["name"] == update_name


# Тест успешного удаления курса
@pytest.mark.django_db
def test_successful_course_deletion(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.delete(f"/courses/{courses[6].id}/")
    assert response.status_code == 204
    assert response.data == None
