import os
from ezkfg import Config


class TestJSON:
    def test_load(self):
        config = Config()
        config.load(os.path.join(os.path.dirname(__file__), "..", "examples", "example_config.json"))

        print(config.dict())

        assert config.a == 1
        assert config.b.c == 2
        assert config.b.d.e == 3
        assert config.c.d.e == 3

    def test_dump(self):
        config = Config()
        config.load(os.path.join(os.path.dirname(__file__), "..", "examples", "example_config.json"))
        config.dump("dump_config.json")
