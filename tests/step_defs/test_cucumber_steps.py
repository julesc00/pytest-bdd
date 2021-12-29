from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then
from cucumbers import CucumberBasket

EXTRA_TYPES = {
    "Number": int,
}
# helper function to avoid adding the test_task() function
scenarios("../features/cucumbers.feature")
partial_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@given(partial_num('the basket has "{initial:Number}" cucumbers'), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(partial_num('"{some:Number}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)


@when(partial_num('"{some:Number}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(partial_num('the basket contains "{total:Number}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total


@given('the basket has "8" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Given the basket has "8" cucumbers')


@given('the basket has "2" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Given the basket has "2" cucumbers')


@when('"4" cucumbers are added to the basket')
def step_impl():
    raise NotImplementedError(u'STEP: When "4" cucumbers are added to the basket')


@then('the basket contains "6" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Then the basket contains "6" cucumbers')


@when('"3" cucumbers are removed from the basket')
def step_impl():
    raise NotImplementedError(u'STEP: When "3" cucumbers are removed from the basket')


@then('the basket contains "5" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Then the basket contains "5" cucumbers')