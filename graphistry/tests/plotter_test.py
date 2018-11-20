import pytest
from graphistry import Plotter

def test_plot():
    p = Plotter() \
        .data(
            edges = None,
            nodes = None
        ) \
        .bind(
            source = 'x'
        ) \
        .plot()

if __name__ == '__main__':
    pytest.main()
