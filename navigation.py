import os
import webapp2
import jinja2
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))

class NavRouterHandler(webapp2.RequestHandler):
    def get(self):
        strurl = str(self.request.url)
        strRoute = strurl.split("/")
        strRoute = strRoute[len(strRoute) - 1]

        if strRoute == "footer":
            template = template_env.get_template('templates/dynamic/navigation/footer.html')
            context = {}
            self.response.write(template.render(context))
        elif strRoute == "sidebar":
            template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
            context = {}
            self.response.write(template.render(context))
        elif strRoute == "header":
            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {}
            self.response.write(template.render(context))
        else:
            pass

app = webapp2.WSGIApplication([
    ('/navigation/.*', NavRouterHandler)

], debug=True)
