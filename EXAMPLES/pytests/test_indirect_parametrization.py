import pytest


class Dog:
    def __init__(self, name):
        self.name = name


@pytest.fixture
def dog(request):
    return Dog(request.param)


@pytest.mark.parametrize(
    'dog',
    ('Lassie', 'Rin-tin-tin', 'Asta', 'Toto'),
    indirect=True
)
def test_dog_name_is_string(dog):
    print(dog.name)
    assert isinstance(dog.name, str)


if __name__ == "__main__":
    pytest.main([__file__, '-s'])

