# app.py
# This is a test commit
# Editing this file one more time to commit to see how action file runs
# test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
