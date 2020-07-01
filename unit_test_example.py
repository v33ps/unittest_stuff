
# This is a function that will say Hello <name> when given a name
# If you give it something other than a string, it wll return an error string
def say_hi(name):
    # make sure the name is a string, if it's not return an error string
    if not isinstance(name, str):
        return "You're not a name!"

    # say hello!
    return "Hello, {}".format(name)



def say_goodbye(name):
    return "Goodbye, {}".format(name)


if __name__ == "__main__":
    greeting = say_hi("bob")
    print(greeting)
