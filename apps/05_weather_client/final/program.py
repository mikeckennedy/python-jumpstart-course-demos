import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    # t = 1, 7, 'cat', [1,2,3]
    # print(t)
    # print(t[1])
    #
    # n1, n2, s, l = t
    # print(n1, n2, s, l)
    # return

    print_the_header()

    # Note: wunderground changed it's URL structure, zipcode no longer works.
    # We need to pass state and city (sorry folks outside the US).
    # You can update the URL for your country.
    state = input('What US state do you want the weather for (e.g. OR)? ')
    city = input('What city in {} (e.g. Portland)? ')

    html = get_html_from_web(state, city)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}.'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_the_header():
    print('---------------------------------')
    print('           WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web(state, city):
    # Note: wunderground changed it's URL structure, zipcode no longer works.
    # We need to pass state and city (sorry folks outside the US).
    # You can update the URL for your country.
    url = 'https://www.wunderground.com/weather/us/{}/{}'.format(
        state.lower().strip(), city.lower().strip())
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCss = 'h1' # <-- Changed from video recording.
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Note: Due to the change in HTML at wunderground we need to cleanup
    # the title a different way:
    loc = soup.find('h1').get_text() \
        .replace(' Weather Conditions', '') \
        .replace('star_ratehome', '')

    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition).lower()
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
