from omegaconf import DictConfig
import hydra
import logging
logger = logging.getLogger(__name__)


@hydra.main(version_base=None,config_path="config",config_name="train",)
def train(cfg_dict: DictConfig):
    print(cfg_dict)
    # cfg = load_typed_root_config(cfg_dict)
    logger.info('war')
    logger.warning('123')





if __name__ == "__main__":
    # torch.set_float32_matmul_precision('high')
    
    train()