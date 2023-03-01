import os
import ezkfg as ez


class TestINI:
    def test_load(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.ini"
            )
        )

        print(config.dict())

        assert config.a == "1"
        assert config.b == "2"
        assert config.d == "3"
        assert config.e == "4"

    def test_dump(self):
        config = ez.load(
            os.path.join(
                os.path.dirname(__file__), "..", "examples", "example_config.ini"
            )
        )
        config.dump("dump_config.ini")
        config_ = ez.load("dump_config.ini")
        for k, v in config.items():
            assert config_[k] == v

        ez.save(config, "dump_config.ini")
        config_ = ez.load("dump_config.ini")
        for k, v in config.items():
            assert config_[k] == v
