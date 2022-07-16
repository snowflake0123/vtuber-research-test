from invoke import task

from src.main import main

@task
def run(c):
  """Run main."""
  main()
