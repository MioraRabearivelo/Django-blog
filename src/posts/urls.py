from django.urls import path

# TODO: In imports there is three sections separated by a empty line
#   imports from python built-ins functions
#   imports from third parties
#   imports from local project
# TODO: You can use the library black to cleanup your project according to Python style standards
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

# TODO: I don't think this app_name is needed here
app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    # TODO: I would be more explicit for those view names
    #   For example: I would replace `create` by `create_post_view`, etc ..
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='edit'),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name='delete'),
]