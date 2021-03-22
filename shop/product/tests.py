from unittest.result import TestResult
from django.test import TestCase
from product.models import AllProduct

# Create your tests here.
# class ProductTestCase(TestCase):

# def test_response_context_hello(self):
#     response = self.client.get('');

#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(response.content, b"Hello")


class AllProductTestCase(TestCase):
    def setUp(self) -> None:
        # setUp mock data
        AllProduct.objects.create(
            product_name='PHP Book',
            product_pricet='300',
            product_detail="Ea ea amet fugiat voluptate ad veniam in amet in fugiat ipsum irure."
        )
        # return super().setUp()

    # Test Models
    def test_all_product_models(self):
        book = AllProduct.objects.get(product_name="PHP Book")

        # print(book.product_name, book.product_pricet)

        self.assertEqual(
            first=book.product_name,
            second='PHP Book',
            msg="product name is :_ PHP Book"
        )
        self.assertEqual(
            first=book.product_pricet,
            second="300",
            msg="price 300 bath"
        )

    # Test Response WebPage
    def test_page_product_views(self):
        response = self.client.get('/')

        self.assertEqual(
            first=response.status_code,
            second="200",
            msg="Load page success 200 OK"
        )
