import gc_bash_translation

def test_calculate_gc_1():
    assert gc_bash_translation.calculate_gc("ATGCGC") == 66

def test_calculate_gc_2():
    assert gc_bash_translation.calculate_gc("ATGCAT") == 33