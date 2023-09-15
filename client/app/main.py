from nicegui import ui, app
import re
import os
import config
import socket
import json
import requests

# Validating phone number format
def correct_format(input_string):
    pattern = r'^[0-9+]+$'

    if re.match(pattern, input_string):
        config.phone_number_valid = True
        send.enable()
        return True

    else:
        config.phone_number_valid = False
        send.disable()
        return False


# Validating code numerical format
def correct_code(input_string):
    pattern = r'^[0-9]+$'

    if re.match(pattern, input_string) or (input_string == ''):
        config.code_valid = True
        send.enable()
        return True

    else:
        config.code_valid = False
        send.disable()
        return False


# Adding plus sign to phone number function
def add_plus(input_string):
    if not input_string.value.startswith('+') and not input_string.value == '':
        return '+' + input_string.value
    else:
        config.p_number = input_string.value
        return input_string.value


# Set code function for code input
def set_code(input_string):
    if config.code_valid:
        config.code = input_string


# Send button function for phone number and code input
def send():
    try:
        if config.phone_number_valid and not config.phone_number_accepted:  # Sending the phone number

            # Encode the phone number message to send
            phone_number_data = {"phone_number": config.p_number}

            # Send a POST request to check the phone number
            response = requests.post(f"{config.server_url}/check_phone", json=phone_number_data)

            if response.status_code == 200:  # Phone in the list
                ui.notify('Phone number accepted')
                config.phone_number_accepted = True
                phone_number.disable()
                code.enable()
            elif response.status_code == 404:  # Phone is not in list
                ui.notify('Phone number not found. Try again')
                config.phone_number_accepted = False
            else:
                ui.notify("Error:", response.status_code, response.text)

        elif config.phone_number_accepted:  # Sending the code

            # Encode the password message to send
            code_data = {"phone_number": config.p_number, "password": config.code}
            # Send a POST request to verify the code
            response = requests.post(f"{config.server_url}/verify_code", json=code_data)

            if response.status_code == 200:
                data = json.loads(response.text)
                config.token = data.get('token')
                config.code_accepted = True

                ui.notify('Token: ' + config.token, close_button='OK')
                #  Reset UI
                config.phone_number_accepted = False
                config.code_accepted = False
                config.p_number = '+79999999999'
                config.code = '123456'
                phone_number.set_value(config.p_number)
                code.set_value("")
                phone_number.enable()
                code.disable()
                send.enable()

            elif response.status_code == 404:
                ui.notify('Code not matched. Try again')
                config.code_accepted = False
            else:
                ui.notify("Error:", response.status_code, response.text)

    except:
        ui.notify('connection error')


#@ui.page('/')

ui.colors()
with ui.card().classes('bg-cyan-300 no-wrap'):
    with ui.row():
        label = ui.label('Please input your phone number and press SEND:')
        with ui.column().classes('w-full justify-evenly no-wrap'):
            phone_number = ui.input(label='Phone Number:', value=config.p_number,
                                    on_change=lambda n: phone_number.set_value(add_plus(n)),
                                    validation={'Non-numerical format': lambda value: correct_format(value)},
                                    placeholder='Enter your phone number').classes('space-x-5 w-64')
            code = ui.input(label='Code:',
                            on_change=lambda n: set_code(n.value),
                            validation={'Non-numerical format': lambda value: correct_code(value)},
                            placeholder='Enter your code').classes('space-x-5 w-64')
            code.disable()
            send = ui.button('send', on_click=send).props('outline size=xm')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Authenticator', host='0.0.0.0', reload=False, show=True,
           storage_secret=os.environ['STORAGE_SECRET'])
