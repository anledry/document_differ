# differ Project
Document differ WAES assignment

## Description
Project provides http interface that accepts JSON base64 encoded binary data on both
endpoints.
Third endpoint returns diff.
 
## Requirements
* Python language
* virtualenv
* URI format for accepting data: \<host>/v1/diff/\<ID>/\<left|right>
* URI format for returning result: \<host>/v1/diff/\<ID>
* Requests use only JSON format. Binary data should be base64 encoded.
* Tests

## Implementation details
* Django frameworkto process http requests
* sqlite for storing data
* JSON Content-Type to provide requied encoded data
* requests module is used for integration tests

## Server deployment

### Install project
* mkdir -p $HOME/virtualenvs
* mkdir $HOME/virtualenvs
* source $HOME/virtualenvs/differ/bin/activate
* mkdir -p $HOME/workspace
* cd $HOME/workspace
* git clone git@github.com:anledry/document_differ.git
* cd document_differ/differ/
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate


### Start the server and the application
* python manage.py runserver

### Stop application
* CTRL+C

### Exit and remove project
* deactivate

## Usage and examples

### Run unit tests
```
$ python diff_test.py

Ran 4 tests in 0.002s

OK

```

### Run manual tests
The test data using for the manual testing was the same that the unit test
```
$ curl -d '{"data":"SEVMTE9XT1JMRDEyMzQ1"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/v1/diff/89/left/
$ curl -d '{"data":"SEVMTE9XT1JMRDEyMzc4"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/v1/diff/89/right/

curl http://127.0.0.1:8000/v1/diff/89/ -X GET

{
  "diff_blocks": {
    "13": 2
  },
  "equal_content": false,
  "equal_size": true
}
```

## License
Feel free to use this code
