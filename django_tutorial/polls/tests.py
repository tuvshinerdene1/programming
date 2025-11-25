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
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text="Past question." , days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question], )

    def test_future_question(self):
        question = create_question(question_text="Future question.",days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
    
    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question],)
    
    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"],[question2,question1],)