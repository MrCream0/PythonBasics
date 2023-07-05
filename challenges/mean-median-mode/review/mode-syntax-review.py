"""Module containing notes for Brandon."""


def main() -> None:
    """Execute the main process."""

    # Appending Data To A List:
    #
    # Once you have your list object, you can append
    # a new element by accessing the *append* method
    # through the list object variable.
    my_list = [1, 4, 2, 3]
    my_list.append(1)
    my_list.append(1)
    print(f"my_list = {my_list}")
    # [1, 4, 2, 3, 1, 1]

    # Using A List Object's *count* Method:
    #
    # The list object has a method called *count* which will
    # give you the frequency (or number of times a thing appears)
    # of a given input element.
    frequency = my_list.count(1)
    print(f"frequency = {frequency}")
    # 3

    # Calculating The Length Of An Iterable:
    #
    # To calculate the length of most iterable objects, you can
    # simply call the built-in *len* function and pass it the
    # iterable.
    length = len(my_list)
    print(f"length = {length}")
    # 6

    # Creating A Set:
    #
    # You can cast most iterables to a set which will
    # remove duplicates and won't be ordered anymore.
    my_set = set(my_list)
    print(f"my_set = {my_set}")  # {1, 4, 3, 2}

    # Understanding The *max* Method:
    #
    # The *max* method is built-in to the language and it can be used
    # to calculate the highest value in a given iterable.  You must
    # pass in an iterable object to the *max* method to use it.
    highest = max(my_set)
    print(f"highest = {highest}")
    # 4

    # Creating A Dictionary:
    #
    # A dictionary can be created (empty initially) by using the
    # curly brackets.
    my_dict = {}
    print(f"my_dict = {my_dict}")
    # {}

    # Setting A Value In An Existing Dictionary:
    #
    # To set a value in a dictionary, you need to know the key
    # that you want to store the value at.  You would then reference
    # the dictionary using square bracket notation with the key
    # inside the brackets, then set that expression equal to
    # the value you want to set.
    my_dict["one"] = 1
    my_dict["two"] = 2
    print(f"my_dict = {my_dict}")
    # {"one": 1, "two": 2}

    # Understand The Dictionary Iterable Methods:
    #
    # There are three methods to focus on which are as follows...

    # 1. The *keys* method
    #     - This returns the keys in the dictionary
    my_dict_keys = my_dict.keys()
    print(f"my_dict_keys = {my_dict_keys}")
    # dict_keys(['one', 'two'])

    # 2. The *values* method
    #     - This returns the values in the dictionary
    my_dict_values = my_dict.values()
    print(f"my_dict_values = {my_dict_values}")
    # dict_values([1, 2])

    # 3. The *items* method
    #     - This returns the (key, value) pairs in the dictionary
    my_dict_items = my_dict.items()
    print(f"my_dict_items = {my_dict_items}")
    # dict_items([('one', 1), ('two', 2)])


if __name__ == "__main__":
    main()
