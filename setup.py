#!/usr/bin/env python
from setuptools import setup, find_packages


packages = find_packages(where="src")
packages.append("asdf_coordinates_schemas.resources")

package_dir = {
    "": "src",
    "asdf_coordinates_schemas.resources": "resources",
}

package_data = {
    "asdf_coordinates_schemas.resources": ["*.yaml", "**/*.yaml", "**/**/*.yaml"],
}

setup(
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
