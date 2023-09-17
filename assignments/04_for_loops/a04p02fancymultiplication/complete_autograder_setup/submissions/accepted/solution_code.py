first = int(input())
second = int(input())

product = 0
for _ in range(1, second + 1):
    product += first

    # Notice how we use the variable name _ for our loop counter.
    # This is a syntactically valid name for a variable,
    # as variables are allowed to begin with an underscore,
    # but the name is far from descriptive, of course.

    # However, we are never referring to this loop counter variable,
    # so its only purpose is to make sure the loop repeats the required number of times.

    # In such cases, it is an established convention to name the variable thus.
    # So well established, in fact, that some automatic tools make use of the fact.
    # Some code assistance tools can detect and inform the programmer
    # when a variable is being defined but never used,
    # as that is often an indication that the variable can be removed entirely,
    # or perhaps that there's a mistake in the code,
    # and the variable should be referenced somewhere.

    # Here, neither case applies, of course.
    # We need this variable to count the iterations,
    # but we don't need to reference it anywhere else
    # (and there are other cases we would want to do this as well,
    # aside from loops, which you'll see later).

    # If we use this special name for the variable,
    # then these automatic tools know to ignore this,
    # and avoid bothering the programmer with warnings.

print(product)
