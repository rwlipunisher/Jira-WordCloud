from jira import JIRA
from dotenv import load_dotenv
import requests
import os


def authenticator():
  '''Retorna o objeto jira para requestes na conta do usuario.'''
    load_dotenv()
    apikey = os.environ['jira_token']
    user = 'usuario de acesso ao jira'
    server = 'https://rafaeltestes.atlassian.net'
    options = { 'server': server }

    jira = JIRA(options, basic_auth=(user, apikey))

    return jira


