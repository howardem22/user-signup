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
import re

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
            margin-right: 1em;
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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
  return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
  return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
  return not email or EMAIL_RE.match(email)


def form_maker(name,email,ue,pe,ve,ee):
    user="<p><label>Username</label><input type='text' name='username' value="+ name +"><span class='error'>"+ue+"</span></p>"
    passw="<p><label>Password</label><input type='password' name='password' value=''><span class='error'>"+pe+"</span></p>"
    validp="<p><label>Verify Password</label><input type='password' name='verify' value=''><span class='error'>"+ve+"</span></p>"
    mail="<p><label>Email (Optional)</label><input type='text' name='email' value="+ email +"><span class='error'>"+ee+"</span></p>"
    form = "<form method='post'><h2>Signup</h2>"+ user + passw + validp + mail +"<input type='submit'></form>"
    return form


class Index(webapp2.RequestHandler):
#creates the blank form  on the main page
    def get(self):
        content = header + form_maker("","","","","","") + footer
        self.response.write(content)

#checks the input data
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        u_error = ""
        p_error = ""
        v_error = ""
        e_error = ""


        if not valid_username(username):
            u_error = "That's not a valid username"


        if not valid_password(password):
            p_error = "That's not a valid password"

        if verify != password:
            v_error = "Password does not match"

        if not valid_email(email):
            e_error = "That's not a valid email"

        if u_error == "" and p_error == "" and v_error == "" and e_error == "":
            self.redirect("/welcome?username=" + username)
        else:
            content = header + form_maker(username,email,u_error,p_error,v_error,e_error) + footer
            self.response.write(content)

class Welcome(webapp2.RequestHandler):
#assuming all inputs are vallid, show the welcome screen
    def get(self):
        username = self.request.get("username")
        self.response.write("<h1>Welcome</h1>")


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
