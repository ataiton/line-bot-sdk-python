# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

import responses

from linebot import (
    LineBotApi
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    @responses.activate
    def test_get_profile(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/profile/user_id',
            json={
                "displayName": "LINE taro",
                "userId": "Uxxxxxxxxxxxxxx...",
                "pictureUrl": "http://obs.line-apps.com/...",
                "statusMessage": "Hello, LINE!"
            },
            status=200
        )

        profile = self.tested.get_profile('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/profile/user_id')
        self.assertEqual(profile.display_name, 'LINE taro')
        self.assertEqual(profile.user_id, 'Uxxxxxxxxxxxxxx...')
        self.assertEqual(profile.picture_url, 'http://obs.line-apps.com/...')
        self.assertEqual(profile.status_message, 'Hello, LINE!')


if __name__ == '__main__':
    unittest.main()
