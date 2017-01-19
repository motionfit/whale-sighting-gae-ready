from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

import webapp2
import hfwwgDB


class MainPage(webapp2.RequestHandler):
    def get(self):

        html = template.render('templates/header.html', {'title': "Report a Possible Sighting"})
        html = html + template.render('templates/form_start.html', {})
        html = html + """

               <tr><th>Name:</th><td><input type="text" name="name" /></td></tr>
               <tr><th>Email:</th><td><input type="text" name="email" /></td></tr>
               <tr><th>Date:</th><td><input type="text" name="date" /></td></tr>
               <tr><th>Time:</th><td><input type="text" name="time" /></td></tr>

               <tr><th>Location:</th><td><textarea name="location"></textarea></td></tr>

               <tr><th>Fin type:</th><td>
                <select name="fin_type">
                    <option value="" selected="selected">-----------</option>
                    <option value="Falcate">Falcate</option>
                    <option value="Triangular">Triangular</option>
                    <option value="Rounded">Rounded</option>
                </select>
                </td></tr>

               <tr><th>Whale type:</th><td>
                <select name="whale_type">
                  <option value="" selected="selected">-----------</option>
                  <option value="Humpback">Humpback</option>
                  <option value="Orca">Orca</option>
                  <option value="Blue">Blue</option>
                  <option value="Killer">Killer</option>
                  <option value="Beluga">Beluga</option>
                  <option value="Fin">Fin</option>
                  <option value="Gray">Gray</option>
                  <option value="Sperm">Sperm</option>
                </select>
               </td></tr>

               <tr><th>Blow type:</th><td>
                <select name="blow_type">
                  <option value="" selected="selected">-----------</option>
                  <option value="Tall">Tall</option>
                  <option value="Bushy">Bushy</option>
                  <option value="Dense">Dense</option>
                </select>
               </td></tr>

               <tr><th>Wave type:</th><td>
                <select name="wave_type">
                 <option value="" selected="selected">-----------</option>
                 <option value="Flat">Flat</option>
                 <option value="Small">Small</option>
                 <option value="Moderate">Moderate</option>
                 <option value="Large">Large</option>
                 <option value="Breaking">Breaking</option>
                 <option value="High">High</option>
                </select>
               </td></tr>
        """
        html = html + template.render('templates/form_end.html', {'sub_title': "Submit Sighting"})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

    def post(self):
        the_sighting = hfwwgDB.Sighting()
        the_sighting.name   = self.request.get('name')
        the_sighting.email  = self.request.get('email')
        the_sighting.date   = self.request.get('date')
        the_sighting.time   = self.request.get('time')
        the_sighting.location   = self.request.get('location')
        the_sighting.fin_type   = self.request.get('fin_type')
        the_sighting.whale_type = self.request.get('whale_type')
        the_sighting.blow_type  = self.request.get('blow_type')
        the_sighting.wave_type  = self.request.get('wave_type')
        the_sighting.which_user = users.get_current_user()
        
        the_sighting.put()

        html = template.render('templates/header.html', {'title': 'Thank you!'})
        html = html + "<p>Thank you for providing your sighting data.</p>"
        html = html + '<p>Enter <a href="/">another sighting</a>.</p></body></html>'

        self.response.out.write(html)

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()
