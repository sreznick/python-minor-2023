text = {'source': 'To be or not to be',
        'n_words': 6,
        'n_letters': 13
       }

def init_text(txt):
    return {'source': txt,
            'n_words': len(txt.split()),
            'n_letters': sum(len(w) for w in txt.split())
           }

data = init_text('To be or not to be')

print(data)
