# apps/konnected/konnectedcommunity/views.py

from rest_framework import viewsets, permissions
from apps.konnected.konnectedcommunity.models import DiscussionThread, Comment
from apps.konnected.konnectedcommunity.serializers import DiscussionThreadSerializer, CommentSerializer

class DiscussionThreadViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les fils de discussion (forum, Q&A) dans le cadre éducatif.
    """
    queryset = DiscussionThread.objects.all()
    serializer_class = DiscussionThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les commentaires sur les discussions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
# apps/kreative/community/views.py

from rest_framework import viewsets, permissions
from apps.kreative.kreativecommunity.models import CommunityPost, PostComment
from apps.kreative.kreativecommunity.serializers import CommunityPostSerializer, PostCommentSerializer

class CommunityPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les posts communautaires.
    Permet de créer, mettre à jour et supprimer des posts autour des arts.
    """
    queryset = CommunityPost.objects.all()
    serializer_class = CommunityPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostCommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les commentaires sur les posts communautaires.
    Permet de créer, mettre à jour et supprimer des commentaires.
    """
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
