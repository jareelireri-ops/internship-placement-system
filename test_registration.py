from auth import register_user


if register_user():
    print("Test passed: User saved to JSON.")
else:
    print("Test failed.")