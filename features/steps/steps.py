import json
import os
import subprocess

import requests
from behave import given, when, then

@given('the example file {f}')
def step_impl(context, f):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    context.files.append(os.path.join(dir_path, '..', f))

@when('I sort by {sorter}')
def step_impl(context, sorter):
    command_args = ['record-manager', '--sort', sorter]
    command_args.extend(context.files)

    context.output = subprocess.check_output(command_args, encoding='utf-8')

@then('the output should match')
def step_impl(context):
    assert context.output.rstrip('\n') == context.text.rstrip('\n')

@given('the example records')
def step_impl(context):
    context.post_body = context.text

@when('I submit the records to the system')
def step_impl(context):
    context.response = requests.post(
        'http://{}/records'.format(context.record_manager_url),
        data=context.post_body)

@then('it should return successfully')
def step_impl(context):
    context.response.raise_for_status()

@when('I get the records sorted by {sorter}')
def step_impl(context, sorter):
    context.response = requests.get(
        'http://{}/records/{}'.format(context.record_manager_url, sorter))

@then('the response should match')
def step_impl(context):
    expected = json.loads(context.text)

    assert context.response.json() == expected