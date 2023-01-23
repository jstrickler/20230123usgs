import time
import requests
import pandas as pd

URL_TEMPLATE = "http://api.macvendors.com/{}"


def main():
    df = pd.read_csv('../DATA/ClientList.csv')
    df['Manufacturer'] = df.apply(get_mfr_by_mac, axis=1)

    print(df)
    print()
    print(df.iloc[-1])


def get_mfr_by_mac(row):
    mac = row['Clients MAC Address']
    url = URL_TEMPLATE.format(mac)
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        mfr = response.text
    else:
        mfr = 'UNKNOWN'
    time.sleep(.2)  # don't over-request from API
    return f"{mfr}"


if __name__ == '__main__':
    main()
