import logging
import requests

from log.logging import LoggingConfig

pipedrive_api_token = "5fde64f8841ac81f4dc1fa031a33c59ad3b32bc4"

def create_new_deal(username, gist):
     
    # Create new deal in CRM
    create_deal_url = "https://rolandtestcompnay.pipedrive.com/api/v1/deals?api_token="
    logging.info("Request to Pipedrive {}".format(create_deal_url))
    create_deal_response = requests.post(create_deal_url + pipedrive_api_token, data={"org_id": gist, "title": username})
    logging.info("Received response from Pipedrive for {} id".format(gist))

    if create_deal_response.status_code == 201:
        logging.info("New deal for gist {} is successfully created in Pipedrive CRM".format(gist))
    else:
        logging.info(
            "Failed to create organization in Pipedrive CRM for user {}. Response code {} {}".format(username, create_deal_response.status_code, create_deal_response))