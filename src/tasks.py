from invoke import task

@task
def start(c):
    c.run("python main.py")

@task
def test(c):
    c.run("pytest")

@task
def coverage_report(c):
    c.run("coverage run -m pytest")
    c.run("coverage html")