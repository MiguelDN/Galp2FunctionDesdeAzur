import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!afsdfasdfasdfasd')

    logging.info('Python timer trigger function ran at %s HOLA Q ASES Cambio en esta solo', utc_timestamp)
