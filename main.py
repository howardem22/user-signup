#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""
class Index(webapp2.RequestHandler):
    def get(self):
        sign_header = "<h2>Signup</h2>"

        user_form = """
        <form method="post">
        <table>
            <tr>
                <td>Username</td>
                <td><input typr="text" name="username" value="{{username}}"></td>
                <td>{{error_username}}</td>
            </tr>

            <tr>
                <td>Password</td>
                <td><input typr="password" name="password" value=""></td>
                <td>{{error_password}}</td>
            </tr>

            <tr>
                <td>Verify Password</td>
                <td><input typr="text" name="password" value=""></td>
                <td>{{error_verify}}</td>
            </tr>

            <tr>
                <td>Email (Optional)</td>
                <td><input typr="text" name="email" value="{{email}}"></td>
                <td>{{error_email}}</td>
            </tr>
        </table>
        <input type="submit">
        </form>
        """
        content = page_header + sign_header + user_form + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
