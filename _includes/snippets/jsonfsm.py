@coroutine
def string_fsm():
    '''
    A coroutine implementing a finite state machine for parsing JSON strings.
    Accepts the string one character at a time, and yields NOT_PARSED_YET until
    the string has been successfully parsed.
    Once the JSON string has been parsed, yields the corresponding Python
    string. The coroutine can't be used after that.
    May raise JSONParseError on malformed strings.
    Expects data with no leading or trailing whitespace (i.e., the first and
    last input characters should be ").
    '''

    value = []

    c = (yield NOT_PARSED_YET)
    if c != '"':
        raise JSONParseError("JSON strings must start with a quote")

    while True:
        c = (yield NOT_PARSED_YET)
        if c == '"':
            # end of string
            break
        elif c == '\\':
            c = (yield NOT_PARSED_YET)
            if c == 'u':
                # unicode 4-digit hexadecimal
                hexval = ""
                for i in range(4):
                    hexval += (yield NOT_PARSED_YET)

                value.append(unichr(int(hexval, 16)))
            elif c == 'b': value.append('\b')
            elif c == 'f': value.append('\f')
            elif c == 'n': value.append('\n')
            elif c == 'r': value.append('\r')
            elif c == 't': value.append('\t')
            elif c in ('"', '\\', '/'): value.append(c)
            else: raise JSONParseError("Invalid escape character")
        else:
            value.append(c)

    yield ''.join(value)
