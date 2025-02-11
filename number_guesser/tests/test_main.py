import pytest
from src.main import text_to_number

def test_text_to_number():
    assert text_to_number("veintiuno") == 21
    assert text_to_number("quinientos treinta y siete") == 537
    assert text_to_number("mil doscientos cuarenta y cinco") == 1245
    assert text_to_number("mil doscientos cuarenta y cinco") != 1246

if __name__ == "__main__":
    pytest.main()
