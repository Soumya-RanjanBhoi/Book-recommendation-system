import gzip
import pickle

with gzip.open('model.pkl.gz', 'wb') as f:
    pickle.dump('books.pkl', f)
