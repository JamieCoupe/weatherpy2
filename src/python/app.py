from flask import Flask, render_template, g, redirect, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient
from weatherpy2.src.python.services import weatherqueryservice


app = Flask(__name__, template_folder='../../web/templates')
app.config["OIDC_CLIENT_SECRETS"] = "../../data/config/client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "asdansdasdqwergfddfdfdfdfdfdfdfdfdfdfdfddfdfsdfwqlk2342834723842934234qjlwdnalsdaksdlashdja"
oidc = OpenIDConnect(app)
okta_client = UsersClient("https://dev-629582.okta.com", "00xsE71AvAQpNB5MV6QFZbTYdIUBzX5errE0Gj6TqH")


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/current")
def current():
    weatherservice = weatherqueryservice.WeatherQueryService()
    g.weather = weatherservice.get_current_weather()
    return render_template("current.html")


@app.route("/hourly")
def hourly():
    weatherservice = weatherqueryservice.WeatherQueryService()
    g.weather = weatherservice.get_current_weather()
    return render_template("hourly.html")


@app.route("/historic")
def historic():
    return render_template("historic.html")


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".current"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))


if __name__ == '__main__':
    app.run(debug=True)