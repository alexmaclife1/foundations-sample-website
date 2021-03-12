# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json, os


def get_color_code(color_name):
    with open(os.path.dirname(__file__) + '/../data/css-color-names.json') as color_list:
        color_dict = json.load(color_list)
        try:
            color_code = color_dict.get(color_name)
        except None:
            color_code = f"The color '{color_name}' Doesn't seem to exist: /"
        return color_code

print(get_color_code("red"))
