"""
This is a small test suite for GeoSPARQL's SHACL validator.

This Python script uses the pySHACL tool (https://pypi.org/project/pyshacl/) to test that example data in this
folder with the GeoSPARQL 1.1 SHACL validator (validator.ttl in the GeoSPARQL 1.1 repository). The data files indicate
with comments in them and also with file naming conventions whether they are expected to be valid or invalid - 
pass or fail validation.

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

To see each file being processed, use the -s flag to allow the testing functions to print the file value:

~$ pytest test_shapes.py --disable-pytest-warnings -s
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


@pytest.mark.parametrize(
    "data_file_path", 
    [
        Path(".") / "S01-valid.ttl",
        Path(".") / "S02-valid.ttl",
        Path(".") / "S03-valid.ttl",
        Path(".") / "S04-valid.ttl",
        # Path(".") / "S05-valid.ttl", -- not tested
        # Path(".") / "S06-valid.ttl", -- not tested
        # Path(".") / "S07-valid.ttl", -- not tested
        # Path(".") / "S08-valid.ttl", -- not tested
        Path(".") / "S09-valid.ttl",
        Path(".") / "S10-valid.ttl",
        Path(".") / "S11-valid.ttl",
        Path(".") / "S12-valid.ttl",
        Path(".") / "S13-valid.ttl",
        Path(".") / "S14-valid.ttl",
        Path(".") / "S15-valid.ttl",
        Path(".") / "S16-valid.ttl",
        Path(".") / "S17-valid.ttl",
        Path(".") / "S18-valid.ttl",
        Path(".") / "S19-valid.ttl",
        Path(".") / "S20-valid.ttl",
        Path(".") / "S21-valid.ttl",
        Path(".") / "S22-valid.ttl",
        Path(".") / "S23-valid.ttl",
        Path(".") / "S24-valid.ttl",
    ]
)
def test_valid(validator_graph, data_file_path):
    print(f"\nTesting {data_file_path}...")
    v = validate(str(data_file_path), shacl_graph=validator_graph, allow_warnings=True, meta_shacl=True)
    assert v[0], f"File {data_file_path.name}, expected to be valid, failed validation with error messages:\n\n{v[2]}"


@pytest.mark.parametrize(
    "data_file_path", 
    [
        Path(".") / "S01-invalid-01.ttl",
        Path(".") / "S01-invalid-02.ttl",
        Path(".") / "S01-invalid-03.ttl",
        Path(".") / "S02-invalid-01.ttl",
        Path(".") / "S02-invalid-02.ttl",
        Path(".") / "S03-invalid.ttl",
        Path(".") / "S04-invalid-01.ttl",
        Path(".") / "S04-invalid-02.ttl",
        # Path(".") / "S05-invalid.ttl", -- not tested
        # Path(".") / "S06-invalid.ttl", -- not tested
        # Path(".") / "S07-invalid.ttl", -- not tested
        # Path(".") / "S08-invalid.ttl", -- not tested
        Path(".") / "S09-invalid.ttl",
        Path(".") / "S10-invalid.ttl",
        Path(".") / "S11-invalid.ttl",
        Path(".") / "S12-invalid.ttl",
        Path(".") / "S13-invalid.ttl",
        Path(".") / "S14-invalid-01.ttl",
        Path(".") / "S14-invalid-02.ttl",
        Path(".") / "S15-invalid-01.ttl",
        Path(".") / "S15-invalid-02.ttl",
        Path(".") / "S16-invalid.ttl",
        Path(".") / "S17-invalid.ttl",
        Path(".") / "S18-invalid.ttl",
        Path(".") / "S19-invalid.ttl",
        # Path(".") / "S20-invalid.ttl", -- no invalid example
        Path(".") / "S21-invalid.ttl",
        Path(".") / "S22-invalid-01.ttl",
        Path(".") / "S22-invalid-02.ttl",
        Path(".") / "S23-invalid-01.ttl",
        Path(".") / "S23-invalid-02.ttl",
        Path(".") / "S24-invalid-01.ttl",
        Path(".") / "S24-invalid-02.ttl",
    ]
)
def test_invalid(validator_graph, data_file_path):
    print(f"\nTesting {data_file_path}...")
    v = validate(str(data_file_path), shacl_graph=validator_graph, allow_warnings=True, meta_shacl=True)
    assert not v[0], f"File {data_file_path.name}, expected to be invalid, failed validation with error messages:\n\n{v[2]}"