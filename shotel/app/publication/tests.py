import uuid
from django.test import TestCase
from django.contrib.auth import get_user_model
from shotel.app.publication.models import Post
from shotel.app.user.models import Address


class TestPostRank(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create(username=f"Luckson_{uuid.uuid4()}", )
        self.address, create = Address.objects.get_or_create(user=self.user, defaults={'country':'Congo'})

        for i in range(3):
            Post.objects.create(author=self.user, content=f'post_{i}')
    
    def test_post_rank(self):
        posts = Post.objects.post_rank(self.user, top_percentile=80)

        self.assertTrue(posts.exists())

        for post in posts:
            print(f"""\n 
                  content: {post.content} \n 
                  popularity: {post.popularity} \n 
                  address: {post.author.address}""")