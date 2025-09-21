def test_requests():
    
    from requests import get
    
def test_numpy():
    imported = True
    try:
        import numpy
    except ModuleNotFoundError:
        imported = False

    assert imported == False

def test_matplotlib():
    imported = True
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        imported = False

    assert imported == False