import os
import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_nb

PATH_TO_ENV = '/home/sagar/embedded_authors/.env'


def notebook(func):
    def wrapper(*args, **kwargs):
        load_dotenv(PATH_TO_ENV)
        if os.environ['NOTEBOOK']:
            func(pbar_type=tqdm_nb, *args, **kwargs)
        else:
            func(pbar_type=tqdm, *args, **kwargs)
    return wrapper()


@notebook
def dict_to_arr(d: dict[dict[float]],
                pbar_on: bool = False,
                **kwargs) -> np.ndarray:

    """
    Converts a dictionary of dictionaries with external keys i and internal keys j corresponding to value
    v into an array A indexed as A[i,j] = v

    :param d: a dictionary of dictionaries
    :param pbar_on: Whether or ont to show the progress bar
    """

    vectors = list()

    if pbar_on:
        pbar = kwargs['pbar_type'](d.values)
    else:
        pbar = d.values

    for author in pbar:
        vectors.append(np.array([author[concept] for concept in author]))

    return np.array(vectors)

@notebook
def author_embedding(M: np.ndarray,
                     pbar_on:bool = False,
                     **kwargs) -> np.ndarray:

    '''
    author_embedding() takes in an array of arbitrary dimension N x M for N values of x and M values of y to create a
    matrix where each row corresponds to the values p(y_i | x_k).

    :param M: a matrix of arbitrary dimension
    :param pbar_on: Whether or ont to show the progress bar
    '''

    #TODO: Double Check that everything here makes sense

    priors = M.sum(axis=0)
    data = M.sum(axis=1)
    total_c = sum(priors)
    total_a = sum(data)

    num_auth, num_con = M.shape

    out = np.zeros((num_auth, num_con))

    if pbar_on:
        pbar = tqdm(range(num_auth))
    else:
        pbar = tqdm(range(num_auth))

    for a in pbar:
        for c in range(num_con):
            if data[a] == 0:
                out[a,c] = 0
            else:
                out[a,c] = M[a,c]/data[a]

    return out
