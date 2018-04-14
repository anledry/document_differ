from django.http import JsonResponse
from rest_framework.decorators import api_view
from app.models import DocumentRight, DocumentLeft
import base64
from diff_functions import get_diff_blocks


def create_document(request, pk, endpoint, DocumentModel):
    response = ""
    try:
        request_data = request.data["data"]
        DocumentModel(pk=pk, data=base64.b64decode(request_data)).save()
        response_data = {"message": "Document created", "endpoint": endpoint, "id": pk}
        response = JsonResponse(response_data)
    except TypeError as e:
        response = JsonResponse({"error": "Invalid base64 format: {}".format(e)})
        response.status_code = 400
    except Exception as e:
        response = JsonResponse({"error": str(e)})
        response.status_code = 400
    return response


@api_view(['POST'])
def right(request, pk):
    """
    Create the documment for the right side of a diff request.
    Args:
        request: The web request.
        pk: The diff request ID
    Returns:
        JSON response for the request.
    """
    if request.method == 'POST':
        return create_document(request, pk, "right", DocumentRight)


@api_view(['POST'])
def left(request, pk):
    """
    Create the documment for the left side of a diff request.
    Args:
        request: The web request.
        pk: The diff request ID
    Returns:
        JSON response for the request.
    """
    if request.method == 'POST':
        return create_document(request, pk, "left", DocumentLeft)


@api_view(['GET'])
def differ(request, pk):
    """
    Get the diff result documment between the right and left side diff request.
    Args:
        request: The web request.
        pk: The diff request ID
    Returns:
        JSON response for the request.
    """
    response = ""
    if request.method == 'GET':
        try:
            document_right = DocumentRight.objects.get(pk=pk)
            document_left = DocumentLeft.objects.get(pk=pk)

            diff_blocks = None
            equal_size = False
            equal_content = False

            if document_right.data == document_left.data:
                equal_size = True
                equal_content = True
            elif len(document_right.data) == len(document_left.data):
                equal_size = True
                diff_blocks = get_diff_blocks(document_right.data, document_left.data)

            response = JsonResponse({"equal_size": equal_size, "equal_content": equal_content, "diff_blocks": diff_blocks})
        except DocumentRight.DoesNotExist as e:
            response = JsonResponse({"error": "Could not compare, missing right side data  "})
        except DocumentLeft.DoesNotExist as e:
            response = JsonResponse({"error": "Could not compare, missing left side data  "})
        except Exception as e:
            response = JsonResponse({"error": str(e)})
            response.status_code = 400
        return response