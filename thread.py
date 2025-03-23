# SPDX-FileCopyrightText: 2024 Andreas Wolf (awolf002@gmail.com)
# SPDX-License-Identifier: Apache-2.0
#
# pylint: disable=import-error
import gdb
import enum
from .common import StructProperty, print_table

class ThreadProperty(StructProperty):
    NAME = ('', 'name', 'get_string_val')
    ENTRY = ('Entry pointer', 'pEntry', 'get_val')
    STATUS = ('State', 'thread_state', 'get_val')
    PRI = ('Thread priority', 'prio', 'get_val')
    AF = ('CPU', 'cpu', 'get_val')
    IDLE = ('Idle Thread', 'is_idle', 'get_val')

class StackProperty(StructProperty):
    START = ('Stack base', 'start', 'get_val')
    SIZE = ('Stack size', 'size', 'get_val')

def get_all_threads():
    current_tcb_arr = []

    try:
        current_tcb_head = gdb.parse_and_eval('_kernel.threads')
    except gdb.error as err:
        print(err, end='\n\n')
        return current_tcb_arr

    while current_tcb_head != 0:
        current_tcb_arr.append(current_tcb_head)
        current_tcb_head = current_tcb_head['next_thread']

    return current_tcb_arr

def get_table_row(thread_ptr):
    row = []
    thread = thread_ptr.referenced_value()
    base = thread['base']
    entry = thread['entry']
    try:
        stack = thread['stack_info']
        got_stack_info = True
    except:
        got_stack_info = False

    fields = thread.type
    for _, item in enumerate(ThreadProperty):
        val = thread
        if not item.exist(fields):
            continue
        row.append(item.value_str(val))

    fields = base.type
    for _, item in enumerate(ThreadProperty):
        val = base
        if not item.exist(fields):
            continue
        row.append(item.value_str(val))

    fields = entry.type
    for _, item in enumerate(ThreadProperty):
        val = entry
        if not item.exist(fields):
            continue
        row.append(item.value_str(val))

    if got_stack_info:
        fields = stack.type
        for _, item in enumerate(StackProperty):
            val = stack
            if not item.exist(fields):
                continue
            row.append(item.value_hex_str(val))

    return row

def print_help(tcb_struct):
    for _, item in enumerate(ThreadProperty):
        item.print_property_help(tcb_struct)
    for _, item in enumerate(StackProperty):
        item.print_property_help(tcb_struct)
    print('')

def get_table_headers(thread_lst):
    row = []
    thread_ptr = thread_lst[0]

    thread = thread_ptr.referenced_value()
    base = thread['base']
    entry = thread['entry']

    try:
        stack = thread['stack_info']
        got_stack_info = True
    except:
        got_stack_info = False

    for _, item in enumerate(ThreadProperty):
        if not item.exist(thread.type):
            continue
        row.append(item.title)
    for _, item in enumerate(ThreadProperty):
        if not item.exist(base.type):
            continue
        row.append(item.title)
    for _, item in enumerate(ThreadProperty):
        if not item.exist(entry.type):
            continue
        row.append(item.title)

    if got_stack_info:
        for _, item in enumerate(StackProperty):
            if not item.exist(stack.type):
                continue
            row.append(item.title)

    return row

def get_table_rows(current_thr):
    table = []
    for _, thread in enumerate(current_thr):
        row = get_table_row(thread)
        table.append(row)
    return table

def show():
    table = []
    headers = []
    current_thr = get_all_threads()
    a_len =  len(current_thr)
    print(f"# threads: {a_len}")

    table_rows = get_table_rows(current_thr)
    table.extend(table_rows)

    if len(table) == 0:
        return

    print_table(table, get_table_headers(current_thr))


class ZephyrThread(gdb.Command):
    """ Generate a print out of the current threads and their states.
    """

    def __init__(self):
        super().__init__('zephyr thread', gdb.COMMAND_USER)

    @staticmethod
    def invoke(_, __):
        show()
