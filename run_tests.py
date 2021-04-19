import os
import sys
sys.path.append("src")

# Tests should be formatted as so:
# tests/<test_name>
#           |-- run_test.py
#           |-- description.py
#           |-- (other content)

# run_test.py -------
# enabled = True # (or False)
# def run():
#     # Import other content and game functions
#     # DO NOT sys.path.append("src")
#     # It might break the framework
#     # Do that in the individual file runner, below
#     # Test goes here, return bool if test passed
#     return True

# if __name__ == "__main__":
#     import sys
#     sys.path.append("src")
#     print(run())

if __name__ == "__main__":
    failures = []
    tests = next(os.walk("tests"))[1]
    print("Running all tests")
    print("(.) = Test passed")
    print("(&) = Test failed")
    print("(*) = Test is disabled")

    for test in tests:
        path = "tests/"+test
        sys.path.append(path)
        import run_test

        if run_test.enabled:
            # Result is boolean if test passed
            try:
                # run returns result of test
                result = run_test.run()
            except Exception as e:
                # If the game crashes, test failed
                result = False

            if result:
                print(".", end="")
            else:
                print("&", end="")
                failures.append(test)
        else:
            print("*", end="")

        sys.path.remove(path)

        try:
            del sys.modules["run_test"]
            del sys.modules["initial_state"]
            del sys.modules["final_state"]
            del sys.modules["strategies"]
        except:
            pass

    print("\nRan all tests!")

    if len(failures) > 0:
        print("The following tests failed:")
        for test in failures:
            print(test)
    else:
        print("All tests passed!")
