def test_numpy():
    import numpy as np

def test_matplotlib():
    import matplotlib.pyplot as plt

def test_requests():   
    imported = True
    try:
        from requests import get
    except ModuleNotFoundError:
        imported = False

    assert imported == False