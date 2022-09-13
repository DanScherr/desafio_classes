class Depena_String:

    def __init__(self, *args) -> None:
        self.sem_espacos = self.del_empty_spaces(args)
        pass

    def del_empty_spaces(tupla: tuple):
        for s in tuple:
            strings = [value for value in s.split(' ') if value!= '']
            strings = ' '.join(strings)
            
        self.sem_espacos = strings
