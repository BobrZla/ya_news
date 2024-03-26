# news/tests/test_routes.py
import unittest
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from news.models import News


# это шпаргалка, ее не трогаем
@unittest.skip('скипаем')
class TestRoutesNoneActive(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # Создаем объект конкретной новости/поста
        cls.news = News.objects.create(title='заголовок', text='текст')

    def test_home_page(self):
        """код теста, проверяющего доступность главной страницы проекта"""
        # Вместо прямого указания адреса
        # получаем его при помощи функции reverse().
        url = reverse('news:home')
        response = self.client.get(url)
        # Проверяем, что код ответа равен статусу OK (он же 200).
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_detail_page(self):
        """код теста, проверяющего доступность отдельного поста"""
        # получаем адрес url этого поста
        url = reverse('news:detail', args=(self.news.id,))
        # ответ браузера при переходе на страницу поста
        response = self.client.get(url)
        # сравниваем ответ браузера со статусом 200/ОК
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(title='Заголовок', text='Текст')

    def test_pages_availability(self):
        urls = (
            ('news:home', None),
            ('news:detail', (self.news.id,)),
            ('users:login', None),
            ('users:logout', None),
            ('users:signup', None),
        )
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
