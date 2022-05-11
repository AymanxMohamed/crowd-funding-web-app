from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    author_picture = serializers.SerializerMethodField('get_author_picture')

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_name(self, comment):
        return comment.owner.first_name + " " + comment.owner.last_name

    def get_author_picture(self, comment):
        return comment.owner.profile_picture.__str__() or None