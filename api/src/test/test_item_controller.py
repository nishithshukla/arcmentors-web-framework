# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.items import Items  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_add_item(self):
        """Test case for add_item

        Add a new item
        """
        body = Item()
        response = self.client.open(
            '/api/v1/item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_items(self):
        """Test case for get_all_items

        Gets all items
        """
        response = self.client.open(
            '/api/v1/item',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_item(self):
        """Test case for get_item

        Get a item
        """
        response = self.client.open(
            '/api/v1/item/{item_id}'.format(item_id='item_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_item(self):
        """Test case for remove_item

        Remove a item
        """
        response = self.client.open(
            '/api/v1/item/{item_id}'.format(item_id='item_id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_item(self):
        """Test case for update_item

        Update and replace an item
        """
        Item = Item()
        response = self.client.open(
            '/api/v1/item/{item_id}'.format(item_id='item_id_example'),
            method='PUT',
            data=json.dumps(Item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
