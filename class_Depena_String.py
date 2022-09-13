class Depena_String:

    def __init__(self, string:str) -> None:
        self._sem_espacos = self.del_empty_spaces(string)
        pass

    def del_empty_spaces(self, string: str):
        if type(string) == str:
            s_no_space = [value.lower().capitalize() for value in string.split(' ') if value!= '']
            s_no_space = ' '.join(s_no_space)
            self.sem_espacos = s_no_space
