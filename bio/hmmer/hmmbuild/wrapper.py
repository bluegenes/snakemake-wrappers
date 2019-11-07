"""Snakemake wrapper for hmmbuild"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2019, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("hmmbuild {extra} {snakemake.output} {snakemake.input} {log}")
