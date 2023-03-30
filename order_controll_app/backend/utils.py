from lxml import etree
from decimal import Decimal

from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import pandas as pd

from .config import GoogleConfig
from . import logger


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
        logger.error(
            f"Getting data from google sheet finished with error: {error}"
        )
        raise requests.exceptions.ConnectionError(
            "Cant get data from google disk!"
        )

    logger.info("Getting data from google was successfull!")
    for key in data[0]:
        if key not in GoogleConfig.COLUMN_NAMES:
            logger.error(f"Field {key} is not valid name for column!")
            raise KeyError(f"Not valid column name ({key}) in google sheet")
    if len(data[0]) != 4:
        logger.error(f"Unexpected numbers of columns: 4 != {len(data[0])}")
        raise ValueError(
            f"Not valid column number ({len(data[0])}) in google sheet"
        )

    data_frame = pd.DataFrame(data[1:], columns=data[0])
    data_frame = data_frame.rename(
        columns={
            "№": "id",
            "заказ №": "order_name",
            "стоимость,$": "price_usd",
            "срок поставки": "expires_in",
        }
    )
    data_frame["expires_in"] = data_frame["expires_in"].apply(
        lambda x: pd.to_datetime(x, format="%d.%m.%Y")
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
    else:
        logger.error(
            "Cant get currency rate from bank, "
            f"response status: {response.status_code}"
        )
    return (None, None)
