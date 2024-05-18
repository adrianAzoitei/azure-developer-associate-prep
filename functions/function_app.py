import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
@app.cosmos_db_input(
    arg_name="inputDocuments", 
    database_name="foo", 
    container_name="bar", 
    partition_key="/foo",
    connection="CosmosDBConnection")
def http_trigger(req: func.HttpRequest, inputDocuments: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    id = req.params.get('id')
    if id:
        doc = inputDocuments[id]
        logging.info(doc)

    if id:
        return func.HttpResponse(f"This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Pass an id in the query string for a personalized response.",
             status_code=200
        )