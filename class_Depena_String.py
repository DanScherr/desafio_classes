# ------------ DEFINING CLASS ------------
from re import search


class Depena_String:


    # TODO: Criar construtor
    def __init__(self, string:str) -> None:
        self._string = self.set_string(string)
        # Defining especial chars to validate strings by its cluster
        self.name_special_chars = '^[a-zA-Z]*$'
        self.cpf_special_chars = '^[0-9]*$'
        pass

    def set_string(self, string: str):
        if (type(string) == str):
            self.string = string
        else:
            raise Exception("\n - ERRO1: Digite um texto.")

    # TODO: Metodo que trata nomes compostos (Deleta nomes vazios e Deixa a primeira leta de cada nome maíuscula e o resto minúscula)
    def nomeComposto(self) -> str:
        # s_no_space = [value.lower().capitalize() for value in string.split(' ') if ( (value != '') and (not value.isnumeric()) )]
        nomeComposto = [value.lower().capitalize()
                        for value in self.string.split(' ') 
                        if ( (value != '') and 
                        (bool((search(self.cpf_special_chars ,value)))) )]
        nomeComposto = ' '.join(nomeComposto)
        return nomeComposto

    def cpf(self) -> str:
        first_dot_condition  = (self.string[:3] == ".")
        second_dot_condition = (self.string[:7] == ".")
        first_hyfen_condition = (self.string[:11] == ".")
        
        if (first_dot_condition and 
            second_dot_condition and 
            first_hyfen_condition):

            cpf_list = [value
                            for value in self.string.split('.') 
                                if ( (value != '') and 
                                    (bool((search(self.name_special_chars ,value)))))]
            
            cpf_string = '.'.join(cpf_list)
            return cpf_string

