import argparse
import boto3
import yaml


parser = argparse.ArgumentParser(prog='trasfer.py', description='script for transfer domains between route53 accounts')
parser.add_argument('--config', '-c', type=str, help='config file path', required=True)
args = parser.parse_args()

config_file = args.config

config = yaml.load(config_file)
