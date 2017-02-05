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
import jinja2
import os

template_path=os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))


class Index(webapp2.RequestHandler):
    def get(self):



        error = self.request.get("error")

        t = jinja_env.get_template("form.html")
        content = t.render(
            username= self.request.get("username"),
            email= self.request.get("email"),
            error= error
        )
        self.response.write(content)

    def post(self):


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
