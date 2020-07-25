from send_email import send_mail
from get_data import get_gdp_data
from pretty_html_table import build_table


def send_country_list():
    gdp_data = get_gdp_data()
    output = build_table(gdp_data, 'blue_light')
    send_mail(output)
    return "Mail sent successfully."


send_country_list()
