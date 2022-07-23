from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response
# 브랜치 파야 해서,,,


class PostListView(views.APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'message': '게시글 목록 조회 성공', 'data': serializer.data})

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '게시글 작성 성공', 'data': serializer.data})
        return Response({'message': '게시글 작성 실패', 'error': serializer.errors})


class PostDetailView(views.APIView):
    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response({'message': '게시글 상세 조회 성공', 'data': serializer.data})

    def put(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '게시글 수정 성공', 'data': serializer.data})
        return Response({'message': '게시글 수정 실패', 'error': serializer.errors})

    def delete(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({'message': '게시글 삭제 성공'})


class CommentView(views.APIView):
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '댓글 작성 성공', 'data': serializer.data})
        return Response({'message': '댓글 작성 실패', 'error': serializer.errors})

    def get(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': '댓글 수정 성공', 'data': serializer.data})
        return Response({'message': '댓글 수정 실패', 'error': serializer.errors})

    def delete(self, request, pk, format=None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response()


class SignUpView(views.APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data})
        return Response({'message': '회원가입 실패', 'error': serializer.errors})


class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.data})
        return Response({'message': "로그인 실패", 'data': serializer.errors})
