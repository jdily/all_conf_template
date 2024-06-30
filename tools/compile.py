import argparse
import os, sys, yaml
from easydict import EasyDict as edict

def parse_args():
    """parse input arguments"""
    parser = argparse.ArgumentParser(description='scorer')
    parser.add_argument('--mode', type=str, default='clean', help='clean, arxiv')
    # parser.add_argument('--arxiv')
    args = parser.parse_args()


def clean(cfg):
    pass

def arxiv(cfg):
    pass

if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    cfg = edict(cfg['default'])
    args = parse_args()
    cfg.mode = args.mode
    if args.mode == 'clean':
        clean(cfg)
    elif args.mode == 'arxiv':
        arxiv(cfg)
    # print(cfg_default)