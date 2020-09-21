# Copyright 2020 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def one_level_function():
    # dummy comment
    # to take up
    # three lines
    return 0


def multiline_args_tuple(
    a,
    b,
    c
):
    # dummy comment
    # to take up
    # three lines
    return 0


def nested_if_statements():
    if True:
        if True:
            # dummy comment
            # to take up
            # three lines
            return 0


def nested_for_statements():
    for x in range(1):
        for y in range(1):
            # dummy comment
            # to take up
            # three lines
            return 0


def nested_with_statements():
    with open(__file__, 'r') as _:
        # dummy comment to take up a line
        return 0


# TODOs
def ending_tuple():
    return (
        # dummy comment
        # to take up
        # three lines
        1,
        2,
        3
    )


def ending_dict():
    return {
        # dummy comment
        # to take up
        # three lines
        'a': 1,
        'b': 2,
        'c': 3
    }


def ending_array():
    return [
        # dummy comment
        # to take up
        # three lines
        1,
        2,
        3
    ]


def ending_list_comp():
    return [x for x
            # dummy comment
            # to take up
            # three lines
            in range(2)]