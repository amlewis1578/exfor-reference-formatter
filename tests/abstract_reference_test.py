from exforrefs.references.abstract_reference import AbstractReference
import pytest

# test that the class exists, but can't be instantiated
def test_abstract_ref():
    with pytest.raises(TypeError):
        obj = AbstractReference({})
