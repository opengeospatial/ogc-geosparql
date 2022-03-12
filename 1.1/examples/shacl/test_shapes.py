"""
This is a small test suite for GeoSPARQL's SHACL validator.

This small Python script uses the pySHACL tool (https://pypi.org/project/pyshacl/) to test that example data in this
folder with the GeoSPARQL 1.1 SHACL validator (validator.ttl in the GeoSPARQL 1.1 repository). The data files indicate
with comments in them and also with file naming conventions whether they are expected to pass or fail validation.

Files ending _valid.ttl are expected to be valid. Files ending _invalid.ttl are expected to be _invalid_. The files
start with the ID of the SHACL rule they are testing. The IDs are present in the IRIs of the SHACL shapes in the
validator file.

This script requires Python 3.7+ and a few standard Python distribution packages. Additionally, the following Python
packages available on the Python Package Index (https://pypi.org) are needed:

* pytest (https://pypi.org/project/pytest/) - a generic Python testing framework
* pyshacl (https://pypi.org/project/pyshacl/) - an RDF validator tool

Using a package manager, installation of just those two packages should allow you to execute these tests.

Running the tests
-----------------
Installing pytest results in a python script called pytest that can be used in this directory like this:

~$ pytest test_shapes.py --disable-pytest-warnings

The --disable-pytest-warnings flag is to hide deeper Python warning messages not needed for general use.

As long as you see no errors, things are working well! Warnings are OK.
"""
import pytest
from pathlib import Path
from pyshacl import validate
from rdflib import Graph


@pytest.fixture
def validator_graph():
    try:
        return Graph().parse(Path(__file__).parent.parent.parent / "validator.ttl")
    except FileNotFoundError:
        print("ERROR: Cannot load the validator graph. "
              "Please check that the path specified for the validator.ttl file is valid")
        exit()


def test_valid(validator_graph):
    for f in Path(".").glob("*-valid.ttl"):
        v = validate(str(f), shacl_graph=validator_graph, allow_warnings=True, meta_shacl=True)
        assert v[0], f"File {f.name}, expected to be valid, failed validation with error messages:\n\n{v[2]}"
