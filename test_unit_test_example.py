
import pytest

# import the function we want to test from the code
from unit_test_example import say_hi



# This `pytest.mark.parametrize` will call the function `test_say_hi()` twice.
# The first time with the parameters "bob" and "Hello, bob". The second time
# with the parameters -1 and "You're not a name!"

# The function `test_say_hi()` will compare the return value from `say_hi(name)`
# and make sure it matches what we passed in as the `expected` parameter
@pytest.mark.parametrize("name, expected", [
    ("bob", "Hello, bob"),
    (-1, "You're not a name!")
])
def test_say_hi(name, expected):
    # make sure the return value from `say_hi()` matches what we expect
    assert say_hi(name) == expected
