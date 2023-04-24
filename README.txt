-------------Wordcloud-Jira Projects

A ideia do projeto é gerar um cloudword destacando as palavras mais usadas nos projetos do jira. 
O script python pega as palavras inputadas pelos usuarios no jira e faz o wordcloud.
Observações: 
-Importante que para pegar todos os projetos da empresa o usuario autenticado deve ter acesso a todo conteudo do jira
-Gerar API Jira consultar 'https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/'
-Voce pode adicionar os campos dos jira que julgar necessario, adicionando os campos na lista 'fields' no arquivo wordcloudjira.py
 o presente codigo so pega o resumo e o titulo do issue( tarefa, epic, etc. ). 
 
 See you soon! :) 
