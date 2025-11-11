import pytest
import subprocess

# -------------------------------
# Functions to test
# -------------------------------
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fourth_power(n):
    return n ** 4

def fifth_power(n):
    return n ** 5


# -------------------------------
# Unit tests (parameterized)
# -------------------------------
@pytest.mark.parametrize("n, expected", [(2, 4), (3, 9), (4, 16), (5, 25)])
def test_square(n, expected):
    assert square(n) == expected

@pytest.mark.parametrize("n, expected", [(2, 8), (3, 27), (4, 64), (5, 125)])
def test_cube(n, expected):
    assert cube(n) == expected

@pytest.mark.parametrize("n, expected", [(2, 16), (3, 81), (4, 256), (5, 625)])
def test_fourth_power(n, expected):
    assert fourth_power(n) == expected

@pytest.mark.parametrize("n, expected", [(2, 32), (3, 243), (4, 1024), (5, 3125)])
def test_fifth_power(n, expected):
    assert fifth_power(n) == expected


def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        cube("string")
    with pytest.raises(TypeError):
        fourth_power("string")
    with pytest.raises(TypeError):
        fifth_power("string")


# -------------------------------
# Code Quality Tests
# -------------------------------
import subprocess
import pytest

@pytest.mark.quality
def test_flake8():
    """Run flake8 linting."""
    result = subprocess.run(["flake8", "src"], capture_output=True, text=True)
    assert result.returncode == 0, f"Flake8 issues found:\n{result.stdout}"

@pytest.mark.quality
def test_pylint():
    """Run pylint checks."""
    result = subprocess.run(["pylint", "src"], capture_output=True, text=True)
    assert result.returncode == 0, f"Pylint issues found:\n{result.stdout}"

@pytest.mark.quality
def test_black_formatting():
    """Ensure black formatting compliance."""
    result = subprocess.run(["black", "--check", "src"], capture_output=True, text=True)
    assert result.returncode == 0, f"Black formatting issues found:\n{result.stdout}"
