__author__ = 'KoicsD'


class UserInterrupt(Exception):
    pass


def user_input(inp_prompt: str, parser_fcn, validator_fcn, data_for_validating: list, parse_err_msg=None):
    s_data = ""
    p_data = []
    while True:
        s_data = input(inp_prompt)
        if s_data == "\quit":
            raise UserInterrupt(inp_prompt)
        try:
            if parser_fcn is None:
                temp = s_data
            else:
                temp = parser_fcn(s_data)
            if validator_fcn is None:
                p_data.append(temp)
                msg = "OK"
            else:
                msg, p_data = validator_fcn(temp, data_for_validating)
            if msg == "OK":
                break
            else:
                print(msg)
        except ValueError as parsing_error:
            if parse_err_msg is not None:
                print(parse_err_msg)
            else:
                print(parsing_error.args[0])
    return p_data
