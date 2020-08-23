
import pytest

# connects our tests with our database
pytestmark = pytest.mark.django_db

from .factories import CheeseFactory
from ..models import Cheese


from ..models import Cheese
def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

