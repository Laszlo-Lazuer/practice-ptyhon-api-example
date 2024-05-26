# practice-ptyhon-api-example


## Notes
- Quick practice project to create an API with Python & Flask

## Testing the API
- Install the dependencies: `pip install -r requirements.txt`
- Start the flask server: `python main.py`

### Available APIs
- `get_user` -> Once you start the server open the provided URL with port and add `/get-user/123??extra="hello"` as an example where we are passing in the captured parameter value `extra`. The response will be displayed in your browser.
- `create_user` -> must be tested outside of the browser IE with Postman. This may be tested with the collection in the resources folder.
