#!/usr/bin/env python
#
#   Copyright 2019 Andrea Bonomi <andrea.bonomi@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the Licens
#

__all__ = [
    'PLUGIN_NAME',
    'MENU_CATEGORY',
    'MENU_LABEL',
    'ROUTE',
    'STATIC',
    'CONFIG_SECTION',
    'SUPPORTED_GIT_COMMANDS',
    'HTTP_200_OK',
    'HTTP_404_NOT_FOUND'
]

PLUGIN_NAME = 'code_editor'
MENU_CATEGORY = 'Admin'
MENU_LABEL = 'DAGs Code Editor'
ROUTE = '/' + PLUGIN_NAME
STATIC = '/static/' + PLUGIN_NAME
CONFIG_SECTION = PLUGIN_NAME + '_plugin'
HTTP_200_OK = 200
HTTP_404_NOT_FOUND = 404
SUPPORTED_GIT_COMMANDS = [
    'add',
    'branch',
    'checkout',
    'commit',
    'diff',
    'log',
    'ls-tree',
    'reset',
    'rm',
    'show',
    'stage',
    'status',
    'tag',
    'unstage'
]