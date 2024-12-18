"""Tässä tiedostossa on projektin invoke tehtävät."""
import os
from invoke import task
from dotenv import load_dotenv

@task
def start(ctx):
    """Käynnistä ohjelma."""
    ctx.run("python3 src/index.py", pty=True)

@task
def init_test_db(ctx):
    """Alusta testitietokanta"""
    load_dotenv(dotenv_path=".env.test")

    database_name = os.getenv("DATABASE_NAME")

    ctx.run(f"DATABASE_NAME={database_name} python3 src/data/initialize_database.py", pty=True)

@task(pre=[init_test_db])
def test(ctx):
    """Alustaa testitiestokannan ja aja testit."""
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    """Aja kaikki testit ja luo testikattavuus."""
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    """Luo testikattavuusraportti, kun testit on ajettu."""
    ctx.run("coverage html", pty=True)

@task
def format(ctx):
    """Muotoile koodi"""
    ctx.run("autopep8 --in-place --recursive src")

@task
def lint(ctx):
    """Aja pylint."""
    ctx.run("pylint src")

@task
def init_db(ctx):
    """Poista nykyiset taulut ja luo uudet."""
    load_dotenv(dotenv_path=".env")
    ctx.run("python3 src/data/initialize_database.py", pty=True)

@task
def fill_db(ctx):
    """Täytä tietokantataulut testidatalla"""
    load_dotenv(dotenv_path=".env")
    ctx.run("python3 src/data/create_test_db_data.py", pty=True)

@task
def open_db(ctx):
    """Avaa tietokanta"""
    load_dotenv(dotenv_path=".env")
    database_name = os.getenv("DATABASE_NAME")
    ctx.run(f"sqlite3 {database_name}", pty=True)

@task
def open_test_db(ctx):
    """Avaa testitietokanta"""
    load_dotenv(dotenv_path=".env.test")
    database_name = os.getenv("DATABASE_NAME")
    ctx.run(f"sqlite3 {database_name}", pty=True)