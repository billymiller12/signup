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
import webapp2, re



class MainHandler(webapp2.RequestHandler):
    def get(self):
        pw_form="""
        <form action="/name" method="post">
            <label for="username">Username</label>
                <input name="name" type="text">
                <br>
            <label for="password">Password</label>
                <input name="password" type="password">
                <br>
            <label for="verify">Verify Password</label>
                <input name="verify" type="password">
                <br>
            <label for="email">Email(Optional)</label>
                <input name="email" type="email">
                <br>
                <input type="submit">
        </form>
        """
        self.response.write(pw_form)

class Response(webapp2.RequestHandler):
    def post(self):
        username= self.request.get("name")
        password= self.request.get("password")
        verify1= self.request.get("verify")
        email1= self.request.get("email")

        if username == "":
            error1= " Please enter a username."
        elif not re.match("^[a-zA-Z0-9_-]{3,20}$", username):
            error1=" Please enter a valid username"
        else:
            error1= ""
        if password != verify1:
            error2= " Passwords do not match."
        else:
            error2= ""

        pw_response_form="""
        <form action= "/name" method= "post">
            <label for="username">Username</label>
                <input name="name" type="text">
                <br>
            <label for="password">Password</label>
                <input name="password" type="password">
                <br>
            <label for="verify">Verify Password</label>
                <input name="verify" type="password">
                <br>
            <label for="email">Email(Optional)</label>
                <input name="email" type="email">
                <br>
                <input type= "submit">
                <br>
                <p class="error">""" + error1 + error2 + """</p>
        </form>
        """
        if error1 != "":
            self.response.write(pw_response_form)
        elif error2 != "":
            self.response.write(pw_response_form)
        else:
            self.response.write("Welcome """ + username + "")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/name', Response)
], debug=True)
