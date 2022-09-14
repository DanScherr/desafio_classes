# ------------ DEFINING CLASS ------------
from multiprocessing.sharedctypes import Value


from re import search

class Depena_String:

    # TODO: Criar construtor

    def __init__(self, string:str) -> None:
        self._string = self.del_empty_spaces(string)
        pass


    # TODO: Metodo que trata nomes compostos (Deleta nomes vazios e Deixa a primeira leta de cada nome maíuscula e o resto minúscula)

    def del_empty_spaces(self, string: str):
        name_special_chars = '^[a-zA-Z]*$'
        if type(string) == str:
            # s_no_space = [value.lower().capitalize() for value in string.split(' ') if ( (value != '') and (not value.isnumeric()) )]
            s_no_space = [value.lower().capitalize() for value in string.split(' ') if ( (value != '') and (bool((search(name_special_chars ,value)))) )]
            s_no_space = ' '.join(s_no_space)
            self.string = s_no_space
        else:
            raise Exception("\n - ERRO1: Digite um texto.")
