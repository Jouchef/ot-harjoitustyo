"""Tässä tiedostossa on projektin invoke tehtävät."""

from invoke import task

@task
def start(ctx):
    """Käynnistä ohjelma."""
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    """pytest"""
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def lint(ctx):
    ctx.run("pylint src")