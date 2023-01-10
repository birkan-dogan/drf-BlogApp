from .models import Category, Blog
from faker import Faker
from datetime import datetime


def run():
    fake = Faker(["en-US"])
    categories = (
        "Information Technologies",
        "Programming",
        "Artificial Intelligence",
        "Deployment",
        "Agile Methodologies"
    )

    for category_id in categories:
        new_category = Category.objects.create(name = category_id)

        for i in range(30):
            Blog.objects.create(category = new_category, title = fake.company(), content = fake.text(), is_published = fake.pybool())