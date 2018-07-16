import os
import subprocess

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