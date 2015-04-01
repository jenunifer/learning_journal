import itertools
import re
import distutils
from mechanize import Browser
br = Browser()


"""  Over 100,000 combinations of 5 digit codes allowing repeat numbers
between 0-9. Removing the possibility of zero at first digit,
new combo formula is at 9x10^5 * """

br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Chrome')]


# Get the search results
br.submit()


# print response.read()


def get_list():
    list = range(10)
    return list


def html(s):
    return "<b>" + s + "</b>"


if __name__ == '__main__':
    br.open("https://www.apps.akc.org//apps/dogreg/index.cfm?useraction=route")
    br.select_form(name="PuppyPinForm")
    combos = itertools.permutations(get_list())
    for x in combos:
        input = [x]
        list = [html(x) for x in input]
        for x in list:
            br["emailAddress"] = 'jen@evergreenherbologist.com'
            br["registrationNumber"] = "SR85263302"
            br["onlinePIN"] = [list]  # (the method here is __setitem__)
