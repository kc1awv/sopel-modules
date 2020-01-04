# coding=utf-8
"""
radioid.py - Sopel RadioID.net Module
Copyright 2020, Steve Miller <smiller@kc1awv.net>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

https://kc1awv.net
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import json
import random
import sys

import requests

from sopel.module import rule, commands, priority, example, unblockable

if sys.version_info.major >= 3:
    unicode = str

protocol = "https"
endpoint = "www.radioid.net"
timeout = 10

def request(urn, key):
    response = requests.get(protocol + "://" + endpoint + "/" + urn, timeout=timeout)
    json = response.json()

    if response.status_code == 200:
        res = json.get("results")
        rep = [sub[key] for sub in res]
        return rep
    else:
        return "Status code " + str(response.status_code)

@commands('duid')
@example('.duid 3122790', '"Callsign for DMR ID is KC1AWV"')
def duid(bot, trigger):
    """Returns the callsign for the requested DMR User ID number"""
    duid = trigger.group(2)
    urn = "api/dmr/user/?id=" + duid
    key = "callsign"

    message = request(urn, key)
    bot.reply("Callsign for DMR User ID " + duid + ": " + str(message))

@commands('ducall')
@example('.ducall KC1AWV', '"ID for callsign is 3122790"')
def ducall(bot, trigger):
    """Returns the DMR User ID(s) for the requested callsign"""
    ducall = trigger.group(2)
    urn = "api/dmr/user/?callsign=" + ducall
    key = "id"

    message = request(urn, key)
    bot.reply("DMR User ID(s) for callsign " + ducall + ": " + str(message))

@commands('drid')
@example('.drid 310458', '"Callsign for DMR Repeater 310458 is KC1AWV"')
def drid(bot, trigger):
    """Returns the callsign for the requested DMR Repeater ID number"""
    drid = trigger.group(2)
    urn = "api/dmr/repeater/?id=" + drid
    key = "callsign"

    message = request(urn, key)
    bot.reply("Callsign for DMR Repeater ID " + drid + ": " + str(message))

@commands('drcall')
@example('.drcall KC1AWV', '"DMR Repeater ID for callsign is 310458"')
def drcall(bot, trigger):
    """Returns the ID(s) for the requested DMR Repeater callsign"""
    drcall = trigger.group(2)
    urn = "api/dmr/repeater/?callsign=" + drcall
    key = "id"

    message = request(urn, key)
    bot.reply("DMR Repeater ID(s) for callsign " + drcall + ": " + str(message))

@commands('nuid')
@example('.nuid 3122790', '"Callsign for NXDN ID is KC1AWV"')
def nuid(bot, trigger):
    """Returns the callsign for the requested NXDN User ID number"""
    nuid = trigger.group(2)
    urn = "api/nxdn/user/?id=" + nuid
    key = "callsign"

    message = request(urn, key)
    bot.reply("Callsign for NXDN User ID " + nuid + ": " + str(message))

@commands('nucall')
@example('.nucall KC1AWV', '"ID for callsign is 3122790"')
def nucall(bot, trigger):
    """Returns the NXDN User ID(s) for the requested callsign"""
    nucall = trigger.group(2)
    urn = "api/nxdn/user/?callsign=" + nucall
    key = "id"

    message = request(urn, key)
    bot.reply("NXDN User ID(s) for callsign " + nucall + ": " + str(message))
