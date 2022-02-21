#!/usr/bin/env python
from pathlib import Path
from setuptools import setup, find_packages


packages = find_packages(where="src")
packages.append("asdf_coordinates_schemas.resources")

package_dir = {
    "": "src",
    "asdf_coordinates_schemas.resources": "resources",
}


def package_yaml_files(directory):
    paths = sorted(Path(directory).rglob("*.yaml"))
    return [str(p.relative_to(directory)) for p in paths]


package_data = {
    "asdf_coordinates_schemas.resources": package_yaml_files("resources"),
}

setup(
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
