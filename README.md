#### CLI tool For RestAPI Testing
Make sure python (preferred python3.7) is added to path.

python --version or python3.7 --version Install virtualenv using pip.
```
 pip install virtualenv 
 ```
 
First create a virtual environment for the project.

```virtualenv -p python3.7 venv or virtualenv venv
     . venv/bin/activate (Linux)
     . venv/Scripts/activate (windows)
 ```
 Run CLI tool using below command
 ```
. [<environment_name>]/Scripts/activate
pip install --editable .
. -->make sure that setup.py is availiable in current directory
 ```
 Parent CLI Command
 ```
 $ sham-restapicli
 output:
    Usage: sham-restapicli [OPTIONS] COMMAND [ARGS]...

   sham-restapicli is Parent command for RestAPI CLI

   sham-restapicli http-get is need one url of api

   sham-restapicli http-post is need two argument url and data in dictionary
   formate

    Options:
      --help  Show this message and exit.
    
    Commands:
      http-delete  This is command for http delete method
      http-get     This is command for HttpGet method
      http-post    This is command for HttpPost method ..Please send data in...
      http-put     This is command for http put method

 ```
 steps to runing subcommand
 
 ```
 $ sham-restapicli --help    ------>sub command for guidance
 $ sham-restapicli http-get <endpoint_url> ------>sub command for get method
 $ sham-restapicli http-post <endpoint_url> <json_formate_data_to_post>-------> sub command for post method
 $ sham-restapicli http-put <endpoint_url> <json_formate_data_to_post>----->sub command for put method
 $ sham-restapicli http-delete <endpoint_url> ----->sub command for delete method
 ```
 ### Setup Linter
create setup.cfg file for  pycodestyle and pep8
generate pylintrc file using below command for pylint
 ```
 pylint --generate-rcfile > .pylintrc
  (change max_length_character to 160 (as per requiremnet))
  
Linter Script:
   create lint.sh file
    run using command sh lint.s
```

#### Unittest
Run unit Test case of app using below command

```
python -m unittest tests
```
 
 
