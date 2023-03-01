import os
from pathlib import Path
import ezkfg as ez


class TestJSON:
    file_path = Path(
        os.path.join(os.path.dirname(__file__), "..", "examples", "example_config.json")
    )

    def test_load(self):

        config = ez.load(self.file_path)

        print(config.dict())

        assert config.a == 1
        assert config.b.c == 2
        assert config.b.d.e == 3
        assert config.c.d.e == 3

    def test_dump(self):
        config = ez.load(self.file_path)
        config.dump("dump_config.json")
        config_ = ez.load("dump_config.json")
        for k, v in config.items():
            assert config_[k] == v

        ez.save(config, "dump_config.json")
        config_ = ez.load("dump_config.json")
        for k, v in config.items():
            assert config_[k] == v
