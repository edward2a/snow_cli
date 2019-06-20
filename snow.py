#!/usr/bin/env python3.7


import argparse
#import json
import pysnow
import snow_cli
import yaml

from pprint import pprint
from types import SimpleNamespace


apis = SimpleNamespace(
    app         = '/table/cmdb_ci_appl',
    change      = '/table/change_request',
    incident    = '/table/incident'
)



def parse_args():
    """The CLI arguments."""
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest='resource', required=True)

    # Global
    p.add_argument('-c', '--config', required=False, default='./snow.yml',
        help='The config file location')

    app     = s.add_parser('app', help='Appication resource')
    app_s   = app.add_subparsers(dest='action', required=True)

    ch      = s.add_parser('change', help='Change resource')
    ch_s    = ch.add_subparsers(dest='action', required=True)

    inc     = s.add_parser('incident', help='Incident resource')
    inc_s   = inc.add_subparsers(dest='action', required=True)


    # App Subparsers
    app_get = app_s.add_parser('get', help='Get an application configuration item')
    app_get_id = app_get.add_mutually_exclusive_group(required=True)
    app_get_id.add_argument('-n', '--name', help='Get the resource by name search')
    app_get_id.add_argument('-i', '--id', help='Get the resource by id')

    # Change Subparsers
    ch_approved = ch_s.add_parser('is-approved?',
        help='Check if a change is in approved state')
    ch_approved.add_argument('-n', '--number', required=True,
        help='The change record number (CHGXXXXXXX)')

    # Incident Subparsers

    return p.parse_args()


def load_config(_file):
    """Load a YAML config file and return a dict."""
    with open(_file) as f:
        return yaml.safe_load(f)


def new_conn(config):
    """Create a ServiceNow connection and return the object."""
    return pysnow.Client(instance=config['host'], user=config['user'], password=config['pass'])


def resource_handler(sn_conn, api):
    """Return an API handler usin the API map."""
    return sn_conn.resource(api_path=apis.__dict__[api])


def main():
    args    = parse_args()
    config  = load_config(args.config)
    sn      = new_conn(config)
    res_h   = resource_handler(sn, args.resource)
    #for r in snow_cli.handler(res_h, args).all():
    #    print(json.dumps(r))
    exit(True != snow_cli.handler(res_h, args))


if __name__ == '__main__':
    main()
