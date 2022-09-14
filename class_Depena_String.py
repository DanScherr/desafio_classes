# ------------ DEFINING CLASS ------------

from re import search


class Depena_String:


    # TODO: Criar construtor
    def __init__(self, string:str) -> None:
        self._string = self.set_string(string)
        pass

    def set_string(self, string: str):
        if (type(string) == str):
            self.string = string
        else:
            raise Exception("\n - ERRO1: Digite um texto.")

    # TODO: Metodo que trata nomes compostos (Deleta nomes vazios e Deixa a primeira leta de cada nome maíuscula e o resto minúscula)
    def nomeComposto(self) -> str:
        name_special_chars = '^[a-zA-Z]*$'
        # s_no_space = [value.lower().capitalize() for value in string.split(' ') if ( (value != '') and (not value.isnumeric()) )]
        nomeComposto = [value.lower().capitalize() for value in self.string.split(' ') if ( (value != '') and (bool((search(name_special_chars ,value)))) )]
        nomeComposto = ' '.join(nomeComposto)
        return nomeComposto
