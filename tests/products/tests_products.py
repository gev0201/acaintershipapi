import pytest

from endpoints.products import Products
from utils.jsonmodels import product_json


@pytest.mark.run(order=1)
def test_get_products(app_config):
    products = Products()
    prod_list = products.get_products(app_config.base_url, 200)
    products.check_products_data_by_length(prod_list, 18)


@pytest.mark.run(order=2)
def test_create_product(app_config):
    products = Products()
    json = product_json.create_product_json("Apple", "Tablet", 1000, 4)
    products.create_product(app_config.base_url, json)


@pytest.mark.run(order=3)
def test_get_products_after_create_item(app_config):
    products = Products()
    prod_list = products.get_products(app_config.base_url, 200)
    products.check_products_data_by_length(prod_list, 19)


@pytest.mark.run(order=4)
def test_edit_product(app_config):
    products = Products()
    id = products.find_id_by_name(app_config.base_url, 200, "Apple")
    json = product_json.update_product_json(id, "Apple_MAC", "Tablet MAC", 1001, 4)
    products.edit_product(app_config.base_url, json)


@pytest.mark.run(order=5)
def test_delete_product(app_config):
    products = Products()
    id = products.find_id_by_name(app_config.base_url, 200, "Apple_MAC")
    json = product_json.delete_product_json(id)
    aaa = products.delete_product(app_config.base_url, json)
    prod_list = products.get_products(app_config.base_url, 200)
    products.check_products_data_by_length(prod_list, 18)
