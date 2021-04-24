from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from django.core.paginator import *
from django.conf import settings

from product.serializers import *
from common.helper import HelperClass


class GetAllProducts(GenericAPIView):

    @classmethod
    def get(self, request):
        _res = {}
        _resStatus = status.HTTP_200_OK
        try:
            _limit = request.GET.get('limit', settings.DEFAULT_LISTING_LIMIT)
            _pageNo = request.GET.get('page', settings.DEFAULT_LISTING_PAGE)

            _productList = Product.objects.filter(is_deleted=False).order_by('-id')
            _paginator = Paginator(_productList, _limit)
            _recordData = _paginator.page(_pageNo).object_list

            _res["itemList"] = ProductLIstSerializer(_recordData, many=True).data
            _res["totalPages"] = _paginator.num_pages
            _res["crntPage"] = _pageNo
            _res["totalRecords"] = _productList.count()
            _res["limit"] = _limit
        except Exception as e:
            print("Error: ", e)
            _resStatus = status.HTTP_500_INTERNAL_SERVER_ERROR
            _res["msg"] = "Error! Please try after some time"
        return Response(_res, status=_resStatus)


class ManageProducts(GenericAPIView):

    @classmethod
    def get(self, request):
        _res = {}
        _resStatus = status.HTTP_200_OK

        _reqItemId = request.GET.get('itemId', None)

        if _reqItemId is not None:
            _productDict = Product.objects.filter(id=_reqItemId).last()
            if _productDict is not None:
                _res["itemDetails"] = ProductLIstSerializer(_productDict).data
            else:
                _resStatus = status.HTTP_400_BAD_REQUEST
                _res['errors'] = {
                    "itemId": "Item Id doesn't valid"
                }
        else:
            _resStatus = status.HTTP_400_BAD_REQUEST
            _res['errors'] = {
                "itemId": "Item Id can't be blank"
            }
        return Response(_res, status=_resStatus)

    @classmethod
    def post(self, request):
        _res = {}
        _resStatus = status.HTTP_200_OK

        _postData = ProductSerializer(data=request.data)
        if _postData.is_valid():
            _postData.save()
            _res["msg"] = "Inventory has been created successfully"
        else:
            _resStatus = status.HTTP_400_BAD_REQUEST
            _res['errors'] = HelperClass.get_json_errors(_postData.errors)
        return Response(_res, status=_resStatus)

    @classmethod
    def patch(self, request):
        _res = {}
        _resStatus = status.HTTP_200_OK
        _reqItemId = request.data.get("id")
        _postData = ProductSerializer(data=request.data)
        if _postData.is_valid():
            _productDict = Product.objects.filter(id=_reqItemId).update(
                title=_postData.data.get('title'),
                brand=_postData.data.get('brand'),
                price=_postData.data.get('price'),
                description=_postData.data.get('description'),
            )
            _res["msg"] = "Inventory has been updated successfully"
        else:
            _resStatus = status.HTTP_400_BAD_REQUEST
            _res['errors'] = HelperClass.get_json_errors(_postData.errors)
        return Response(_res, status=_resStatus)


class RemoveProducts(GenericAPIView):
    @classmethod
    def delete(self, request, item_id: any = None):
        _res = {}
        _resStatus = status.HTTP_200_OK

        if item_id is not None:
            _instance = Product.objects.filter(id=item_id).last()
            if _instance is not None:
                _instance.is_deleted = True
                _instance.save()

                _res["msg"] = "Inventory has been removed successfully"
            else:
                _resStatus = status.HTTP_400_BAD_REQUEST
                _res["errors"] = {
                    "itemId": "Inventory Id doesn't valid"
                }
        else:
            _resStatus = status.HTTP_400_BAD_REQUEST
            _res["errors"] = {
                "itemId": "Inventory Id can't be blank"
            }
        return Response(_res, status=_resStatus)
