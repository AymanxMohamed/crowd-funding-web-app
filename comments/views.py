from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from comments.models import Comment
from comments.serializers import CommentSerializer

@api_view(['GET'])
def api_comments_list(request):
    comments = Comment.objects.all()
    serialiezed_comments = CommentSerializer(comments, many=True)
    return Response(serialiezed_comments.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_get_comment_by_id(request, id):
    comment = get_object_or_404(Comment, id=id)
    serlialized_comment = CommentSerializer(comment)
    return Response(serlialized_comment.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_create_comment(request):
    serialized_comment = CommentSerializer(data=request.data)
    if serialized_comment.is_valid():
        serialized_comment.save()
        return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
    return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    serialized_comment = CommentSerializer(instance=comment, data=request.data)
    if serialized_comment.is_valid():
        serialized_comment.save()
        return Response(serialized_comment.data, status=status.HTTP_200_OK)
    return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['delete'])
def api_delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return Response('Comment deleted', status=status.HTTP_200_OK)