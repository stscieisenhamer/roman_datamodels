from pathlib import Path

import pytest

from roman_datamodels import filetype

DATA_DIRECTORY = Path(__file__).parent / "data"


@pytest.mark.filterwarnings("ignore:ERFA function.*")
def test_filetype():
    file_1 = filetype.check(DATA_DIRECTORY / "empty.json")
    file_2 = filetype.check(DATA_DIRECTORY / "example_schema.json")
    file_3 = filetype.check(open(DATA_DIRECTORY / "fake.json"))
    file_4 = filetype.check(DATA_DIRECTORY / "empty.asdf")
    file_5 = filetype.check(DATA_DIRECTORY / "pluto.asdf")
    file_6 = filetype.check(open(DATA_DIRECTORY / "pluto.asdf", "rb"))
    file_7 = filetype.check(DATA_DIRECTORY / "fake.asdf")
    file_8 = filetype.check(open(DATA_DIRECTORY / "fake.asdf"))
    file_9 = filetype.check(str(DATA_DIRECTORY / "pluto.asdf"))

    assert file_1 == "asn"
    assert file_2 == "asn"
    assert file_3 == "asn"
    assert file_3 == "asn"
    assert file_4 == "asdf"
    assert file_5 == "asdf"
    assert file_6 == "asdf"
    assert file_7 == "asdf"
    assert file_8 == "asn"
    assert file_9 == "asdf"

    with pytest.raises(ValueError):
        filetype.check(DATA_DIRECTORY / "empty.txt")

    with pytest.raises(ValueError):
        filetype.check(2)

    with pytest.raises(ValueError):
        filetype.check("test")
