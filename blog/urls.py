from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home, name = 'home-path'),
    # CRUD Post
    path('createPost/', views.createPost_view, name = 'createPost-path'),
    path('listPost/', views.retrievePosts_view, name = 'retrievePosts_view-path'),
    path('detailPost/<int:post_pk>', views.detail_view, name = 'detail_view-path'),
    path('updatePost/<int:post_pk>', views.updatePost_view, name = 'updatePost_view-path'),
    path('deletePost/<int:post_pk>', views.deletePost_view, name = 'deletePost_view-path'),

    # CRUD Contribution
    path('createContribution/<int:post_pk>', views.creatContribution_view, name = 'creatContribution_view-path'),
    path('listPostContributions/<int:post_pk>', views.retrievePostContributions_View, name = 'retrievePostContributions_View-path'),
    path('updatePostContributions/<int:contrib_pk>', views.updatePostContributions_view, name = 'updatePostContributions_view-path'),
    path('deletePostContributions/<int:contrib_pk>', views.deletePostContribution_view, name = 'deletePostContribution_view-path'),





]
