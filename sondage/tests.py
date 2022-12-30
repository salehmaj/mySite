import datetime

from django.test import TestCase
from django.utils import timezone

from sondage.models import Question


# Create your tests here.

class QuestionModelTests(TestCase):
    def test_published_recently_with_future_date(self):
        """
            published_recently va retunrer flase pour les pub_date à l'avenire
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)
