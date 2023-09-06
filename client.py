from nicegui import ui
import re
import config
import socket
import json


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

    if not input_string == '':
        if re.match(pattern, input_string):
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
    if config.phone_number_valid and not config.code_accepted:
        json_data = json.dumps({'phone_number': config.p_number})
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((config.HOST, config.PORT))
                client_socket.send(json_data.encode())
                data = client_socket.recv(1024)

                if data.decode() == '200':
                    print('Phone number accepted')
                    config.phone_number_accepted = True
                    phone_number.disable()
                    code.enable()
            except ConnectionRefusedError:
                print('Connection refused')

            finally:
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()


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
            # code.disable()
            send = ui.button('send', on_click=send).props('outline size=xm')

if __name__ == "__main__":
    ui.run(title='Authenticator', host='127.0.0.1', reload=False, show=True)
    # ui.run(title='Authenticator', reload=True, show=True) - this is for deployment with uvicorn/gunicorn
