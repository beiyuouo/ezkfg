import os
import pickle
from ezkfg import Config


class TestSerialzation:
    def test_serialzation(self):
        config = Config()
        config.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.yaml"
            )
        )
        with open("dump_config.pickle", "wb") as f:
            pickle.dump(config, f)
        with open("dump_config.pickle", "rb") as f:
            config_ = pickle.load(f)
        for k, v in config.items():
            assert config_[k] == v

        assert config_.__frozen__ == config.__frozen__
