# ServiceNow Command Line Interface (snow-cli)

This is (at the moment) a sample implementation of a CLI tool targeted at simplifying programatic access for integration.

Currently using only user/password access, but the library this is based on, pysnow, supports tokens, which will be implemented at some stage here, along with access to request credentials stored in Hashicorp Vault.

## Example usage

Create a snow.yml config file in the same directoy as the snow.py (see snow.yml.example).

#### Help
```
$ ./snow.py -h
usage: snow.py [-h] [-c CONFIG] {app,change,incident} ...

positional arguments:
  {app,change,incident}
    app                 Appication resource
    change              Change resource
    incident            Incident resource

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        The config file location


$ ./snow.py app -h
usage: snow.py app [-h] {get} ...

positional arguments:
  {get}
    get       Get an application configuration item

optional arguments:
  -h, --help  show this help message and exit

```

#### Get an application record
```
$ ./snow.py app get -n 'CMS App FLX'

{"tcp_port": "", "skip_sync": "false", "operational_status": "1", "running_process_command": "", "pid": "", "sys_updated_on": "2010-11-25 11:13:47", "running_process_key_parameters": "", "rp_command_hash": "", "discovery_source": "", "first_discovered": "", "sys_updated_by": "felix.bait", "due_in": "", "install_directory": "", "sys_created_on": "2010-11-25 10:40:31", "sys_domain": {"link": "https://dev78021.service-now.com/api/now/table/sys_user_group/global", "value": "global"}, "used_for": "Production", "install_date": "", "is_clustered": "false", "gl_account": "", "invoice_number": "", "sys_created_by": "felix.bait", "warranty_expiration": "", "asset_tag": "", "fqdn": "", "change_control": "", "owned_by": "", "checked_out": "", "rp_key_parameters_hash": "", "sys_domain_path": "/", "version": "", "delivery_date": "", "maintenance_schedule": {"link": "https://dev78021.service-now.com/api/now/table/cmn_schedule/a618d80e0a0a0b53150f5245edbeb5b6", "value": "a618d80e0a0a0b53150f5245edbeb5b6"}, "install_status": "1", "cost_center": "", "supported_by": "", "dns_domain": "", "name": "CMS App FLX", "assigned": "", "purchase_date": "", "subcategory": "", "short_description": "", "assignment_group": "", "managed_by": "", "edition": "", "can_print": "false", "last_discovered": "", "sys_class_name": "cmdb_ci_appl", "manufacturer": "", "sys_id": "829e953a0ad3370200af63483498b1ea", "po_number": "", "checked_in": "", "sys_class_path": "/!!/!(", "mac_address": "", "vendor": "", "company": "", "justification": "", "model_number": "", "department": "", "config_file": "", "assigned_to": "", "start_date": "", "comments": "", "cost": "", "sys_mod_count": "1", "monitor": "false", "serial_number": "", "ip_address": "", "model_id": "", "sys_tags": "", "cost_cc": "USD", "order_date": "", "schedule": "", "support_group": "", "due": "", "correlation_id": "", "unverified": "false", "attributes": "", "location": "", "asset": "", "category": "", "fault_count": "0", "config_directory": "", "lease_id": ""}
```

#### Check a change is approved
```
$ ./snow.py change is-approved? -n CHG0000094; echo $?
STATE=REQUESTED
1

$ ./snow.py change is-approved? -n CHG0040005; echo $?
STATE=APPROVED
0
```
