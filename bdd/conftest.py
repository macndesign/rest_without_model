import pytest


@pytest.fixture
def w():
    class World:
        pass
    world = World()
    return world
