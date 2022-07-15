from ezkfg import Config


class TestArgs:
    def test_args(self):
        config = Config()
        config.load(["--model=resnet18", "--batch-size=32", "--lr=0.01"])

        print(config.dict())

        assert config.model == "resnet18"
        assert config.batch_size == "32"
        assert config.lr == "0.01"
        assert config.get("epoch") == None
