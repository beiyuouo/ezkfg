import os
from ezkfg import Config


class TestConfig:
    def test_instruction(self):
        config = Config({"a": 1, "b": {"c": 2}})
        assert config.a == 1
        assert config.b.c == 2

        config.a = 3
        assert config.a == 3

        config["d.e.f"] = 3
        assert config["d.e.f"] == 3
        assert config.d.e.f == 3

    def test_laod(self):
        config = Config()
        config.load(os.path.join(os.path.dirname(__file__), "..", "examples", "example_config.json"))

    def test_dump(self):
        config = Config()
