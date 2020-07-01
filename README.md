# unittest_stuff

There are two files, `unit_test_example.py` and `test_unit_test_example.py`.
`unit_test_example.py` is our code that we want to test
`test_unit_test_example.py` holds all the unit test code. By convention, unit test code should be put in files started with `test_`

# Running
Run the command
`pytest`

while in this folder. You will see something like this if everything went correctly
```
$ pytest
=============================================== test session starts ================================================
platform darwin -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /Users/smcconnell/Desktop/unittest_stuff, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 2 items                                                                                                  

test_unit_test_example.py ..                                                                                 [100%]

============================================= 2 passed in 0.06 seconds =============================================
```

# Part 2
Now that you have seen it run with all success, add the following code snippet to the bottom of `test_unit_test_example.py`

```
from unit_test_example import say_goodbye
@pytest.mark.parametrize("name, expected", [
    ("bob", "Goodbye, bob"),
    (-1, "You're not a name!")
])
def test_say_bye(name, expected):
    # make sure the return value from `say_hi()` matches what we expect
    assert say_goodbye(name) == expected
```

And run `pytest` again.

This time you should see something like this:
```
$ pytest
=============================================== test session starts ================================================
platform darwin -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /Users/smcconnell/Desktop/unittest_stuff, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 4 items                                                                                                  

test_unit_test_example.py ...F                                                                               [100%]

===================================================== FAILURES =====================================================
_______________________________________ test_say_bye[-1-You're not a name!] ________________________________________

name = -1, expected = "You're not a name!"

    @pytest.mark.parametrize("name, expected", [
        ("bob", "Goodbye, bob"),
        (-1, "You're not a name!")
    ])
    def test_say_bye(name, expected):
        # make sure the return value from `say_hi()` matches what we expect
>       assert say_goodbye(name) == expected
E       assert 'Goodbye, -1' == "You're not a name!"
E         - Goodbye, -1
E         + You're not a name!

test_unit_test_example.py:32: AssertionError
======================================== 1 failed, 3 passed in 0.08 seconds ========================================

```

Here you can see that one of your tests failed.
See below for an explanation
```
>       assert say_goodbye(name) == expected
E       assert "You're not a name!" == 'Goodbye, -1'
E         - You're not a name!
E         + Goodbye, -1
```
The first line shows you what line in your unit test failed.
The second line shows you what values the variables had in them when it failed
The third line tells you that we expected the string `You're not a name!`
The fourth line tells us that we got the string `Goodbye, -1`

So from our unit test we learned that the function `say_goodbye` is not checking to make sure the value it gets is a string.
