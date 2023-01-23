#!/usr/bin/python
import pytest
from president import President
from datetime import date


def test_president_one_last_name_is_george():
    p = President(1)
    assert p.first_name == "George"


@pytest.mark.parametrize('term_number', range(1, 46))
def test_date_fields_return_dates_or_none(term_number):
        p = President(term_number)
        assert isinstance(p.birth_date, date) or p.birth_date is None
        assert isinstance(p.death_date, date) or p.death_date is None
        assert isinstance(p.term_start_date, date) or p.term_start_date is None
        assert isinstance(p.term_end_date, date) or p.term_end_date is None

@pytest.mark.parametrize('invalid_term', [-1, 0, 46, 1000])
def test_invalid_term_raises_error(invalid_term):
    with pytest.raises(ValueError):
            p = President(invalid_term)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
