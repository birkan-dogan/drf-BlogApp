from rest_framework.viewsets import ModelViewSet
from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly  # custom permission

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]
    permission_classes = [IsAdminOrReadOnly]  #  permission_classes = [IsAdminUser | ReadOnly]


class BlogView(ModelViewSet):
    queryset = Blog.objects.filter(is_published = True)
    serializer_class = BlogSerializer
    filterset_fields = ["category"]
    search_fields = ["title", "content"]
    permission_classes = [IsAuthenticatedOrReadOnly]


