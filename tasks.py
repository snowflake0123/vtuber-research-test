from invoke import task

from src.main import main

QUESTIONNAIRE_PATH = "./questionnaire"

@task
def run(c):
  """Run main."""
  main(QUESTIONNAIRE_PATH)
