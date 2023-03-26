import json

from base.base_api import BaseApi

endpoint = "/api_testing/product/"
get_products_endpoint = endpoint + "read.php"
create_product_endpoint = endpoint + "create.php"
get_product_endpoint = endpoint + "read.php"
update_product_endpoint = endpoint + "update.php"
delete_product_endpoint = endpoint + "delete.php"


class Products(BaseApi):

    def get_products(self, url, expected_status_code, product_name=None):
        if product_name is None:
            response = self.get_request(url + get_products_endpoint)
            self.check_status_code(response, expected_status_code)
            list = self.get_json_value_by_key(response, "$.records..id")
            return list
        else:
            response = self.get_request(url + get_products_endpoint)
            self.check_status_code(response, expected_status_code)
            prod_names = self.get_json_value_by_key(response, "$.records..name")
            for prod_name in prod_names:
                if prod_name == product_name:
                    assert prod_name == product_name
        return response

    def find_id_by_name(self, url, expected_status_code, product_name=None):
        response = self.get_products(url, expected_status_code, product_name)
        data_dict = json.loads(response.text)
        for record in data_dict['records']:
            if record['name'] == product_name:
                return record['id']
        return None

    def check_products_data_by_length(self, data, length):
        assert len(data) == length

    def create_product(self, url, json):
        response = self.post_request(url + create_product_endpoint, json)
        self.check_status_code(response, 201)

    def edit_product(self, url, json):
        response = self.put_request(url + update_product_endpoint, json)
        self.check_status_code(response, 200)

    def delete_product(self, url, json):
        response = self.delete_request(url + delete_product_endpoint, json)
        self.check_status_code(response, 200)
        return response.text

