import logging
from os import getenv
from pprint import pprint as pp

import datafabric

if __name__ == "__main__":
    apikey = getenv("DF_APIKEY")
    apiurl = getenv("DF_APIURL")

    df = datafabric.Datafabric(apiurl,
                               apikey,
                               log_format=None,
                               user_agent="sdk-example/0.2")  # required

    df.logger.setLevel(logging.DEBUG)

    '''
        list all subscriptions for a given agent.
    '''
    response_add_sub = df.list_subscriptions()
    pp(response_add_sub)

    '''
        subscribtion add request.
    '''
    response_add_sub = df.subscribe(dataset="wavewatch*", event_subject="*:abandoned",
                                    topic_arn="arn:aws:sns:eu-west-1:576899322567:df-test-sns-topic")
    pp(response_add_sub)

    '''
        delete subscription, requires a unique subscription_id, 
        contained in the subscribe add response.
        
            response_add_sub["data"]["items"][0]["id"]
    '''
    subscription_id = response_add_sub["data"]["items"][0]["id"]
    pp(df.delete_subscription(subscription_id))
