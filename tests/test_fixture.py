import pytest
def test1(fix):
    pass

@pytest.mark.usefixtures("fix")
def test2():
    pass