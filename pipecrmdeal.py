import logging
import requests

pipedrive_api_token = "5fde64f8841ac81f4dc1fa031a33c59ad3b32bc4"

log = logging.getLogger("RolandTest")


def create_new_deal(username, gist):
     
    # Create new deal in CRM
    create_deal_url = "https://rolandtestcompnay.pipedrive.com/api/v1/deals?api_token="
    log.info("Request to Pipedrive {}".format(create_deal_url))
    create_deal_response = requests.post(create_deal_url + pipedrive_api_token, data={"org_id": gist, "title": username})
    log.info("Received response from Pipedrive for {} id".format(gist))

    if create_deal_response.status_code == 201:
        log.info("New deal for gist {} is successfully created in Pipedrive CRM".format(gist))
    else:
        log.info(
            "Failed to create organization in Pipedrive CRM for user {}. Response code {} {}".format(username, create_deal_response.status_code, create_deal_response))