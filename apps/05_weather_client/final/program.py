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

    code = input('What zipcode do you want the weather for (97201)? ')

    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

    # display for the forecast


def print_the_header():
    print('---------------------------------')
    print('           WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
