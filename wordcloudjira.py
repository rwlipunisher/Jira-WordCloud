from auth import authenticator
import matplotlib.pyplot as plt
from wordcloud import WordCloud

jira = authenticator() #autheticando acesso ao jira. 

def allwords(fields):
  '''Recebe argumento lista de campos do jira que sao inputs de usuario
  e retorna string com todas as palavras usadas em todos os projetos'''
    word = ' '
    projects = jira.projects()
    for i in projects:
        t = jira.search_issues('project='+str(i))
        for j in t:
            for s in fields:
                if str(j.get_field(s)) != 'None':
                    word = word + str(j.get_field(s)) + ' '
    return word

def wcshow(wordc):
  '''recebe um conjunto de palavras em uma string e salva a imagem wordcloud'''
    #stopwords = ['palavras', 'ignoradas', 'no cloudword'] + list(STOPWORDS)
    wordc = WordCloud(background_color='white', height=600, width=800).generate(wordc)
    #wordc = WordCloud(stopwords=stopwords, background_color='white', height=600, width=800).generate(wordc) #incluindo stopwords
    plt.imshow(wordc)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('output.png')
    #return wordc 



# word = allwords(['summary', 'description'])
# wcshow(word)
