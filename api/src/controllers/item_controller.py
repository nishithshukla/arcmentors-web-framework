import connexion
import six

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.items import Items  # noqa: E501
from swagger_server import util


def add_item(body):  # noqa: E501
    """Add a new item

     # noqa: E501

    :param body: Item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_items():  # noqa: E501
    """Gets all items

     # noqa: E501


    :rtype: Items
    """
    return 'do some magic!'


def get_item(item_id):  # noqa: E501
    """Get a item

     # noqa: E501

    :param item_id: The id of the item to retrieve
    :type item_id: str

    :rtype: Item
    """
    return 'do some magic!'


def remove_item(item_id):  # noqa: E501
    """Remove a item

     # noqa: E501

    :param item_id: The id of the item to be removed
    :type item_id: str

    :rtype: None
    """
    return 'do some magic!'


def update_item(item_id, Item):  # noqa: E501
    """Update and replace an item

     # noqa: E501

    :param item_id: The id of the item to be update
    :type item_id: str
    :param Item: 
    :type Item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
