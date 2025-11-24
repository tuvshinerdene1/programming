import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse

class QuestionModelTests(TestCase):
    def test_was_published_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pub_date = time)
        self.assertIs(futureQuestion.was_published_recently(), False)

    def test_was_published_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        oldQuestion = Question(pub_date = time)
        self.assertIs(oldQuestion.was_published_recently(),False)

    def test_was_published_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recentQuestion = Question(pub_date = time)
        self.assertIs(recentQuestion.was_published_recently(), True)
def create_question(question_text, days):
    time = timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
