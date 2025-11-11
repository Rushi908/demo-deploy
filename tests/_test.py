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
@pytest.mark.quality
def test_flake8():
    """Check code style using flake8"""
    result = subprocess.run(
        ["flake8", "--max-line-length=100", "_test.py"],  # ✅ run only on this file
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Flake8 issues found:\n{result.stdout}")


@pytest.mark.quality
def test_pylint():
    """Check code style using pylint"""
    result = subprocess.run(
        ["pylint", "--disable=R,C", "_test.py"],  # ✅ lint this file only
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Pylint issues found:\n{result.stdout}")


@pytest.mark.quality
def test_black_formatting():
    """Check formatting with Black"""
    result = subprocess.run(
        ["black", "--check", "_test.py"],  # ✅ check this file
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Black formatting issues found:\n{result.stdout}")
