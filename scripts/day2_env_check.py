import importlib

MODULES = [
    'pyats', 'genie', 'pytest', 'nornir', 'netmiko',
    'napalm', 'ncclient', 'requests', 'yaml', 'jinja2',
]

failed = []
for name in MODULES:
    try:
        mod = importlib.import_module(name)
        print(f'OK   {name:10} {getattr(mod, "__version__", "n/a")}')
    except Exception as exc:
        failed.append(name)
        print(f'FAIL {name:10} {exc}')

print('All good' if not failed else f'Fix these first: {failed}')
