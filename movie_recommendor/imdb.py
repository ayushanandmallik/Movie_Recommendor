from omdbapi.movie_search import GetMovie


movie= GetMovie(api_key='12d68b8b')


def reverse_string(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
#print(reverse_string('Avengers'))
def movieinfo(name):
    return movie.get_movie(reverse_string(name))



