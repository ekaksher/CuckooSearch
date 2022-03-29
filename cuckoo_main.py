class CuckooProblem():
    def __init__(self,**kwargs):
            self.__upper_boundary = kwargs.get('upper_boundary', 4.)
            self.__lower_boundary = kwargs.get('lower_boundary', 0.)
            self.__alpha = kwargs.pop('alpha', 1)
            self.__max_generations = kwargs.pop('max_generations', 10)
            self.__lambda = kwargs.pop('lambda', 1.5)
            self.__p_a = kwargs.pop('p_a', .1)
            self.__function = kwargs['function']
            kwargs['iteration_number'] = self.__max_generations
            self._visualizer = Visualizer(**kwargs)