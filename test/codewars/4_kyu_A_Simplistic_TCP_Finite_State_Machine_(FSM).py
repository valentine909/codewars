"""
https://www.codewars.com/kata/54acc128329e634e9a000362
"""


EVENTS_DICT = {'RCV_ACK': [('SYN_RCVD', 'ESTABLISHED'), ('FIN_WAIT_1', 'FIN_WAIT_2'), ('CLOSING', 'TIME_WAIT'), ('LAST_ACK', 'CLOSED')],
               'APP_PASSIVE_OPEN': [('CLOSED', 'LISTEN')],
               'APP_ACTIVE_OPEN': [('CLOSED', 'SYN_SENT')],
               'RCV_SYN': [('LISTEN', 'SYN_RCVD'), ('SYN_SENT', 'SYN_RCVD')],
               'APP_SEND': [('LISTEN', 'SYN_SENT')],
               'APP_CLOSE': [('LISTEN', 'CLOSED'), ('SYN_RCVD', 'FIN_WAIT_1'), ('SYN_SENT', 'CLOSED'), ('ESTABLISHED', 'FIN_WAIT_1'), ('CLOSE_WAIT', 'LAST_ACK')],
               'RCV_SYN_ACK': [('SYN_SENT', 'ESTABLISHED')],
               'RCV_FIN': [('ESTABLISHED', 'CLOSE_WAIT'), ('FIN_WAIT_1', 'CLOSING'), ('FIN_WAIT_2', 'TIME_WAIT')],
               'RCV_FIN_ACK': [('FIN_WAIT_1', 'TIME_WAIT')],
               'APP_TIMEOUT': [('TIME_WAIT', 'CLOSED')]}


def traverse_TCP_states(events):
    state = "CLOSED"
    for event in events:
        is_correct = False
        for outcome in EVENTS_DICT[event]:
            if state == outcome[0]:
                state = outcome[1]
                is_correct = True
        if not is_correct:
            return 'ERROR'
    return state
