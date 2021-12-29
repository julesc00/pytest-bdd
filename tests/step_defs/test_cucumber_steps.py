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
