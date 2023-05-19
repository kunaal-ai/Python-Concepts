"""_summary_
"""
from functions.arbitrary_arguments import arbitrary_arguments


def test_arbirtary_arguments():
    """_summary_"""
    assert (
        arbitrary_arguments("python", 3, "a", "r", "g", "s")
        == "language = python rating is 3 and extra details ('a', 'r', 'g', 's')"
    )
