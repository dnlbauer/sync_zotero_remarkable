from setuptools import setup, find_packages

install_reqs = [line.strip() for line in open("requirements.txt").readlines()]
packs = find_packages(exclude=["bin"])

setup(
    name="sync_zotero_rm",
    version="0.0.1",
    author="Daniel Bauer",
    description="Sync zotero collections to remarkable devices",
    install_requires=install_reqs,
    scripts=["bin/sync_zotero_rm"],
    packages=packs
)