import math

from app.embeddings import embed


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    return dot / (norm_a * norm_b)


def test_embed_dimension():
    assert len(embed("hello")) == 384


def test_embed_distinct_and_cosine_range():
    cat = embed("cat")
    dog = embed("dog")
    assert cat != dog
    sim = cosine_similarity(cat, dog)
    assert 0.0 < sim < 1.0
