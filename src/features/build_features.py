from datetime import datetime


class Author:

    def __init__(self,
                 author_id: 'Author ID on OpenAlex',
                 name: str = None,
                 orcid: str = None,
                 publication_titles: list[str] = None,
                 inverted_abstracts: list[str]  = None,
                 publication_dates: list[datetime] = None,
                 ngrams: list[str] = None,
                 concepts: list[int] = None,
                 **kwargs
                 ):
        
        """
        The Author object holds all the relevant textual information about an author as received from OpenAlex.

        This class is simply a container and fields must be filled.
        
        :param author_id: 'Author ID on OpenAlex'
        :param name: 'Full name of the author' 
        :param orcid: 'ORCID' 
        :param publication_titles: 'Titles from publications retrieved by API'
        :param inverted_abstracts: 'Inverted abstracts received from API' 
        :param publication_dates: 'Dates of paper publications received from API' 
        :param ngrams: 'N-gram list as collected from API' 
        :param concepts: 'author concept list from API' 
=
        """

        self.author_id = author_id
        self.name = name
        self.orcid = orcid
        self.titles = publication_titles
        self.abstracts = inverted_abstracts
        self.publication_dates = publication_dates
        self.ngrams = ngrams
        self.concepts = concepts

        for key in kwargs.keys():
            self.key = kwargs.get(key)