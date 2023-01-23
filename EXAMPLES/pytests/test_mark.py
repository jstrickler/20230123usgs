import pytest

@pytest.mark.alpha  # Mark with label alpha
def test_one():
    assert 1

@pytest.mark.alpha  # Mark with label alpha
def test_two():
    assert 1

@pytest.mark.beta  # Mark with label beta
def test_three():
    assert 1

if __name__ == '__main__':
    pytest.main([__file__, '-m alpha'])  # Only tests marked with alpha will run (equivalent to 'pytest -m alpha' on command line)

