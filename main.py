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

header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
        input {
            margin-left: 1em;
        }
    </style>
</head>
<body>
"""

footer = """
</body>
</html>
"""

def form_maker(name,email):
    user="<p><label>Username</label><input type='text' name='username' value="+ name +"></p>"
    passw="<p><label>Password</label><input type='password' name='password' value=''></p>"
    validp="<p><label>Verify Password</label><input type='password' name='verify' value=''></p>"
    mail="<p><label>Email (Optional)</label><input type='text' name='email' value="+ email +"></p>"
    submit="<input type='submit'>"
    form = "<form method='post'><h2>Signup</h2>"+ user + passw + validp + mail + submit +"</form>"
    return form


class Index(webapp2.RequestHandler):
#creates the blank form  on the main page
    def get(self):
        content = header + form_maker("","") + footer
        self.response.write(content)

#checks the input data
    def post(self):
        pass

class Welcome(webapp2.RequestHandler):
#assuming all inputs are vallid, show the welcome screen
    def get(self):
        username = self.response.get("username")
        self.response.write("Welcome, "+ username)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
