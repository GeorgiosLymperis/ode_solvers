import numpy as np

class Solver1D:
    '''
    Base class for one dimensional ODE solvers.
    '''
    def __init__(self, function, h=0.01, n_steps=1000, t0=0):
        '''
        Initialize the solver.

        Parameters:
        -----------
        function: Function
            Function in the right hand
        h: float
            The time step.
        n_steps: int
            The number of time steps.
        t0: float
            The initial time.
        '''
        if not callable(function):
            raise TypeError("function must be callable")
        if h <= 0:
            raise ValueError("Time step h must be positive")
        if n_steps <= 0:
            raise ValueError("Number of steps must be positive")

        self.function = function
        self.h = h
        self.n_steps = int(n_steps)
        self.t = np.zeros((self.n_steps,), dtype=float)
        self.t[0] = t0
        self.y = np.zeros((self.n_steps,), dtype=float)

    def solve(self, **kwargs):
        '''
        Solve the system.

        Parameters:
        -----------
        y0: array_like
            The initial condition.
        '''
        raise NotImplementedError('solve method must be implemented in subclass')

    def plot_solution(self, **kwargs):
        '''
        Plot the solution.
        '''
        raise NotImplementedError('plot_solution method must be implemented in subclass')

class Result:
    '''
    Result of the solver.
    '''
    def __init__(self,**kwargs):
        self.__dict__.update(**kwargs)
    
class Euler(Solver1D):
    '''
    Euler solver.
    '''
    def solve(self, y0=0):
        '''
        Solve the system using Euler's method.
        '''
        self.y[0] = y0
        for i in range(1, self.n_steps):
            self.t[i] = self.t[i-1] + self.h
            self.y[i] = self.y[i-1] + self.h * self.function(self.t[i-1], self.y[i-1])

        result = {}
        result['t'] = self.t
        result['sol'] = self.y
        result['steps'] = self.n_steps
        return Result(**result)

    def plot_solution(self, show=True):
        '''
        Plot the solution.
        '''
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(self.t, self.y)
        ax.set_xlabel('t')
        ax.set_ylabel('y')
        if show:
            plt.show()
        else:
            plt.close(fig)
        return fig, ax

