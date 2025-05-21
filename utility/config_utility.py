from omegaconf import DictConfig, OmegaConf
from dacite import Config, from_dict
from pathlib import Path

TYPE_HOOKS = {
    Path: Path,
}


T = TypeVar("T")



@dataclass
class TrainCfg:
    Root: Path



def load_typed_config(
    cfg: DictConfig,
    data_class: Type[T],
    extra_type_hooks: dict = {},
) -> T:
    return from_dict(
        data_class,
        OmegaConf.to_container(cfg),
        config=Config(type_hooks={**TYPE_HOOKS, **extra_type_hooks}),
    )


def separate_loss_cfg_wrappers(joined: dict) -> list[LossCfgWrapper]:
    # The dummy allows the union to be converted.
    @dataclass
    class Dummy:
        dummy: LossCfgWrapper

    return [
        load_typed_config(DictConfig({"dummy": {k: v}}), Dummy).dummy
        for k, v in joined.items()
    ]


def load_typed_root_config(cfg):
    return load_typed_config(
        cfg,
        TrainCfg,
        {list[LossCfgWrapper]: separate_loss_cfg_wrappers},
    )
