
def wiki_url(*, lang, name):
    return "https://{0}.wikipedia.org/wiki/{1}".format(lang, name)

print(wiki_url(lang='en', name='Python_(programming_language)'))
#print(wiki_url(lang='en', 'Python_(programming_language)'))  # некорректно
#print(wiki_url('en', name='Python_(programming_language)'))  # некорректно
#print(wiki_url('en', 'Python_(programming_language)'))       # некорректно

