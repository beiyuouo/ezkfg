from ezkfg import Config


class TestConfig:
    def test_read(self):
        config = Config()
        config.load("examples/config.json")
        assert 1 == 0
