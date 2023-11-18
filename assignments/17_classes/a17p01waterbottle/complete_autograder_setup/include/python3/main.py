from importlib import import_module
from pathlib import Path

CLASS_NAME = "WaterBottle"


def main():
    test_waterbottle()


def test_waterbottle():
    WaterBottle = get_class()
    callables = {
        "__init__": test_waterbottle_init,
        "__str__": test_waterbottle_str,
        "fill": test_waterbottle_fill,
        "drink": test_waterbottle_drink,
    }

    callable_name = input()
    callables[callable_name](WaterBottle)


def test_waterbottle_init(WaterBottle):
    assert hasattr(
        WaterBottle, "__init__"
    ), f"Could not find member function '__init__' of class 'WaterBottle'."

    parameters = WaterBottle.__init__.__code__.co_varnames
    assert "max_capacity" in parameters, (
        f"Could not find parameter 'max_capacity'"
        "in member function '__init__' of class 'WaterBottle'.",
    )
    assert len(parameters) == 2, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )
    assert (
        parameters[1] == "max_capacity"
    ), f"Parameter 'max_capacity' not found in its expected position."

    default = eval(input())
    try:
        if default:
            instance = WaterBottle()
        else:
            max_capacity = float(input())
            instance = WaterBottle(max_capacity)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    for attribute in "max_capacity", "current_contents":
        assert hasattr(instance, attribute), (
            f"Could not find attribute '{attribute}'"
            "in instance of class 'WaterBottle'."
        )

    print(
        f"Bottle created.",
        f" Capacity: {instance.max_capacity:.2f}L.",
        f" Contents: {instance.current_contents:.2f}L.",
        sep="\n",
    )

    return instance


def test_waterbottle_str(WaterBottle) -> None:
    assert hasattr(
        WaterBottle, "__str__"
    ), f"Could not find member function '__str__' of class 'WaterBottle'."

    instance = test_waterbottle_init(WaterBottle)

    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    print(representation)


def test_waterbottle_fill(WaterBottle):
    assert hasattr(
        WaterBottle, "fill"
    ), f"Could not find member function 'fill' of class 'WaterBottle'."

    instance = test_waterbottle_init(WaterBottle)

    try:
        result = instance.fill()
    except Exception as e:
        print(f"Error filling waterbottle: {e}")
        raise

    assert (
        result is None
    ), f"Function 'fill' should not return a value but returned `{repr(result)}`"

    print(
        f"Bottle filled.",
        f" Contents: {instance.current_contents:.2f}L.",
        f" Capacity: {instance.max_capacity:.2f}L.",
        sep="\n",
    )
    try:
        print(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    return instance


def test_waterbottle_drink(WaterBottle) -> None:
    assert hasattr(
        WaterBottle, "drink"
    ), f"Could not find member function 'drink' of class 'WaterBottle'."

    instance = test_waterbottle_fill(WaterBottle)

    amount = float(input())
    try:
        result = instance.drink(amount)
    except Exception as e:
        print(f"Error drinking from waterbottle: {e}")
        raise

    assert (
        result is not None
    ), f"Function 'drink' should return a value but returned None."

    print(
        f"Bottle sipped.",
        f" Received: {result:.2f}L.",
        f" Contents: {instance.current_contents:.2f}L.",
        f" Capacity: {instance.max_capacity:.2f}L.",
        sep="\n",
    )

    try:
        print(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise


def get_class(name=CLASS_NAME):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Could not find class '{name}'.")


def load_modules():
    modules = []
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
