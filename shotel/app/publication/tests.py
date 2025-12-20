import uuid
from django.test import TestCase
from django.contrib.auth import get_user_model
from shotel.app.publication.models import Post
from shotel.app.user.models import Address
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Post, LikePost, Comment


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


class TestPostAPI(APITestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create(username="Fiston", email="fiston@gmail.com")
        self.post = Post.objects.create(author=self.user, content="Voici mon premier Post")

        self.url = f"/api/v1/post/rank/"
        self.url2 = f"/api/v1/post/post-like/{self.post.id}/"

    def test_can_get_post_data(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_user_can_like_or_unlike_post(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url2)
        response2 = self.client.post(self.url2)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.post.post_likes.exists())
        self.assertEqual(response2.status_code, 201)
            
    def test_post_comment(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'content': "C'est vraiment tres bien comme conseille",
        }

        response = self.client.post(
            f"/api/v1/post/comment-create/{self.post.id}/",
            data, format='json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 1)
        print(f"Count: ", Comment.objects.count())

        response2 = self.client.get(f"/api/v1/post/comment-list/{self.post.id}/")
        
        self.assertEqual(response2.status_code, 200)

