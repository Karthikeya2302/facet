import pytest

from app.rag.cache import SemanticCache

_ANSWER = "Project Nightingale is a $12M acquisition of Stride Payments."


def test_cache_hit_exact():
    c = SemanticCache()
    c.write("ceo", "what is project nightingale", _ANSWER)
    assert c.lookup("ceo", "what is project nightingale") == _ANSWER


def test_cache_hit_similar_phrasing():
    c = SemanticCache()
    c.write("ceo", "what is project nightingale", _ANSWER)
    # "what exactly is project nightingale" scores ~0.978 cosine with MiniLM-L6-v2
    assert c.lookup("ceo", "what exactly is project nightingale") == _ANSWER


def test_cache_miss_different_topic():
    c = SemanticCache()
    c.write("ceo", "what is project nightingale", _ANSWER)
    assert c.lookup("ceo", "how do I book a vacation day") is None


def test_cache_miss_wrong_role():
    c = SemanticCache()
    c.write("ceo", "what is project nightingale", _ANSWER)
    # Same query, different role → miss
    assert c.lookup("hr", "what is project nightingale") is None


def test_cache_clear():
    c = SemanticCache()
    c.write("ceo", "what is project nightingale", _ANSWER)
    c.clear()
    assert c.lookup("ceo", "what is project nightingale") is None
    assert c.lookup("ceo", "tell me about project nightingale") is None
