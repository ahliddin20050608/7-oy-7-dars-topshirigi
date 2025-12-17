from django.urls import path
from .views import BookAPIView,BookDetailAPIView, ArticleAPIView, ArticleDetailAPIView, PostAPIView, PostDELETEUPDATEDETAILView, AuthorAPIView, AuthorDELETEUPDATEDETAILView

urlpatterns = [
    path("books/", BookAPIView.as_view()),
    path("books/<int:pk>/", BookDetailAPIView.as_view()),

    path("articles/", ArticleAPIView.as_view()),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view()),

    path("posts/", PostAPIView.as_view()),
    path("posts/<int:pk>/", PostDELETEUPDATEDETAILView.as_view()),

    path("authors/", AuthorAPIView.as_view()),
    path("authors/<int:pk>/", AuthorDELETEUPDATEDETAILView.as_view()),
]
