import json

def handler(res_h, args):
    cli_h = {
        'app': {
            'get': app_get
        },

        'change': {
            'is-approved?': ch_is_approved
        },

        'incident': {
            'get': inc_get
        }
    }

    return cli_h[args.resource][args.action](res_h, args)


def app_get(res_h, args):
    if args.name is not None:
        resp = res_h.get(query='name={}'.format(args.name)).all()
    elif args.id is not None:
        resp = res_h.get(query='sys_id={}'.format(args.id)).all()
    else:
        return False

    # If records, print, else print empty
    if len(resp) > 0:
        for r in resp:
            print(json.dumps(r))
        return True
    else:
        print('{}')
        return False


def ch_is_approved(res_h, args):
    record = res_h.get(query='number={}'.format(args.number))
    if record['approval'] == 'approved':
        print('STATE=APPROVED')
        return True
    else:
        print('STATE={}'.format(record['approval'].upper()))
        return False

def inc_get(res_h, args):
    pass
