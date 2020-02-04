from setuptools import setup, find_packages

setup(
    
    name = 'RestAPI_CLI',
    version = '0.1',
    package = find_packages(),
    include_package_data = True,
    install_requires = [ 
        'Click',
        'requests',
    ],
    entry_points = '''
        [console_scripts]
        sham-restapicli = src.childcommandpackage.child_commands:parent
        
    ''',
)