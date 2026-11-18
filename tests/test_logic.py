import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot.catalog import find_products

def test_socket():
    assert find_products("нужна умная розетка с расписанием")[0]["id"] == "sock"

def test_vote():
    assert find_products("нужно голосование жильцов и кворум")[0]["id"] == "eknot_vote"

def test_empty():
    assert find_products("привет") == []

if __name__ == "__main__":
    test_socket(); test_vote(); test_empty(); print("OK: 3/3 тестов прошли")
