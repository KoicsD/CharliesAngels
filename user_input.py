__author__ = 'KoicsD'


class UserInterrupt(Exception):
    pass


def user_input(inp_prompt: str, parser_fcn, inp_args: list, parse_err_msg=None):
    cli_str = ""
    ret_vals = []
    while True:
        cli_str = input(inp_prompt)
        if cli_str == "\quit":
            raise UserInterrupt(inp_prompt)
        try:
            ret_vals = parser_fcn(cli_str, inp_args)
            break
        except ValueError as parsing_error:
            if parse_err_msg is not None:
                print(parse_err_msg)
            else:
                print(parsing_error.args[0])
    return ret_vals
