import os

def before_feature(context, feature):
    if 'record_manager_url' in os.environ:
        context.record_manager_url = os.environ['record_manager_url']
    else:
        context.record_manager_url = 'app:5000'


def before_scenario(context, scenario):
    context.files = []