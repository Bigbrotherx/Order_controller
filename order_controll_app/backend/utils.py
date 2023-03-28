from lxml import etree
from decimal import Decimal

from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import pandas as pd

from .config import GoogleConfig


def get_data_from_google() -> pd.DataFrame:
    try:
        credentials = service_account.Credentials.from_service_account_file(
            GoogleConfig.SERVICE_ACCOUNT_FILE, scopes=GoogleConfig.SCOPES
        )
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()
        data = (
            sheet.values()
            .get(spreadsheetId=GoogleConfig.FILE_ID, range="Лист1")
            .execute()
            .get("values")
        )
    except Exception as error:
        # TODO Log
        print(error)
    else:
        data_frame = pd.DataFrame(data[1:], columns=data[0])

        data_frame = data_frame.rename(
            columns={
                "№": "id",
                "заказ №": "order_name",
                "стоимость,$": "price_usd",
                "срок поставки": "expires_in",
            }
        )
        return data_frame


def get_currency_rate():
    """
    В связи с недоступностью официального сайта ЦБ РФ
    Используется альтернативный источник получения котировок.
    """
    response = requests.get("https://www.cbr-xml-daily.ru/daily.xml")
    if response.ok:
        resp_xml_content = response.content
        root = etree.XML(resp_xml_content)
        for tag in root:
            if tag.find("NumCode").text == "840":
                usd_value = Decimal(tag.find("Value").text.replace(",", "."))
                name = tag.find("Name").text
                return (name, usd_value)
    return (None, None)
