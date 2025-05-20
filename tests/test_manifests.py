"""
Test that the manifest file is correctly structured and refers
to schemas that exist.
"""

import asdf
import yaml


def test_manifest(manifest_path):
    content = manifest_path.read_bytes()
    manifest = yaml.safe_load(content)
    schema = asdf.schema.load_schema("asdf://asdf-format.org/core/schemas/extension_manifest-1.0.0")

    asdf.schema.validate(manifest, schema=schema)

    for tag in manifest.get("tags", []):
        # Check that the schema exists:
        if "schema_uri" in tag:
            assert tag["schema_uri"] in asdf.get_config().resource_manager


def test_manifest_tag_order(latest_manifest):
    """Tags should be sorted alphabetically"""
    tag_uris = [tag_def["tag_uri"] for tag_def in latest_manifest["tags"]]
    assert tag_uris == sorted(tag_uris)


def test_tags_match_schemas(latest_manifest):
    """Check that tag and schema versions match"""
    for tag_def in latest_manifest["tags"]:
        tag_uri = tag_def["tag_uri"]
        schema_uri = tag_def["schema_uri"]
        assert tag_uri.split(":")[-1] in schema_uri


def test_uses_latest_schemas(latest_manifest, latest_schema_uris):
    """The latest manifest should always use the latest schemas"""
    for tag_def in latest_manifest["tags"]:
        schema_uri = tag_def["schema_uri"]
        assert schema_uri in latest_schema_uris
