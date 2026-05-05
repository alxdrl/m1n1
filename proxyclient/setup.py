from __future__ import annotations

from setuptools import setup

from packaging.version import Version
from setuptools_scm import ScmVersion

import logging


# Suppress the spurious "pyproject.toml does not contain a tool.setuptools_scm section"
# warning: config is intentionally kept in setup.py to allow a callable version_scheme.
logging.getLogger("setuptools_scm").setLevel(logging.ERROR)


def fork_post_dev_scheme(version: ScmVersion) -> str:
    tag = Version(str(version.tag))

    if version.exact and tag.post is not None:
        return f"{tag}"

    distance = version.distance or 0

    base = tag.base_version
    if tag.pre is not None:
        base += f"{tag.pre[0]}{tag.pre[1]}"

    if tag.post is None:
        post = 100
    else:
        post = ((tag.post // 100) + 1) * 100

    basever = f"{base}.post{post}"

    if version.exact:
        return basever

    if version.dirty:
        return f"{basever}.dev{distance}+dirty"
    
    return f"{basever}.dev{distance}"

setup(
    use_scm_version={
        "tag_regex": r"^(?:proxyclient/)?v(?P<version>.+)$",
        "version_scheme": fork_post_dev_scheme,
        "local_scheme": "no-local-version",
        "write_to": "m1n1/_version.py",
        "search_parent_directories": True,
    }
)