# Blog Exporter
Exports blog posts into pdf

## Running the app
### Pre-requisites
`python3` and `pip3` are installed.
Chrome's Save as PDF - Print dialog does not work in Selenium running inside a Docker container. 
```
./run-app.sh
```

## Running the tests
```
./run-tests.sh
```

## Known Issues
-  The Print Preview could stop loading, resulting in time-out. You can then resume running the application by setting the last indexed page in `website.save_as_pdf`.

# Libraries
- [Selenium Python](https://selenium-python.readthedocs.io/)
- [wait-for-it script](https://github.com/vishnubob/wait-for-it)