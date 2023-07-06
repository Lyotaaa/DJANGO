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
def test_first_course_check(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[6].id
    course_name = courses[6].name
    response = client.get(f"/courses/{courses[6].pk}/")
    assert response.status_code == 200
    assert response.data["id"] == course_id
    assert response.data["name"] == course_name
