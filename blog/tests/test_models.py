from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from config.utils.slugify_ua import slugify
import os

from blog.models import Tag, Post, Category, PostImage, Comment

User = get_user_model()
password = os.environ.get('TEST_PASSWORD')


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name='NewTag')
        self.assertEqual(tag.name, 'NewTag')
        self.assertEqual(tag.slug, 'newtag')

    def test_tag_str_method(self):
        tag = Tag.objects.create(name='Str Method')
        self.assertEqual(str(tag), 'Str Method')

    def test_slug_if_set_manually(self):
        tag = Tag.objects.create(name='Manual Slug', slug='custom-slug')
        self.assertEqual(tag.slug, 'custom-slug')

    def test_unique_name(self):
        Tag.objects.create(name='Unique')
        with self.assertRaises(Exception):
            Tag.objects.create(name='Unique')

    def test_unique_slug(self):
        Tag.objects.create(name='Unique Slug', slug='uni_slug')
        with self.assertRaises(Exception):
            Tag.objects.create(name='Another', slug='uni_slug')


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.com', password=password
        )
        self.category = Category.objects.create(name='TestCategory')
        self.tag1 = Tag.objects.create(name='TagTest1')
        self.tag2 = Tag.objects.create(name='TagTest2')

    def test_post_creation_and_str(self):
        post = Post.objects.create(
            title='This is test post title',
            content='Test is test content',
            author=self.user,
            category=self.category,
        )
        post.tags.set([self.tag1, self.tag2])
        self.assertEqual(str(post), 'This is test post title')
        self.assertEqual(post.author.email, 'testuser@test.com')
        self.assertEqual(post.category.name, 'TestCategory')
        self.assertEqual(post.tags.count(), 2)

    def test_slug_autogeneration(self):
        post1 = Post.objects.create(
            title='Unique Slug Test', content='...', author=self.user
        )
        post2 = Post.objects.create(
            title='Unique Slug Test', content='...', author=self.user
        )
        self.assertEqual(post1.slug, 'unique-slug-test')
        self.assertEqual(post2.slug, 'unique-slug-test-1')

    def test_get_absolute_url(self):
        post = Post.objects.create(
            title='URL Post Test', content='...', author=self.user
        )
        expected_url = reverse('post_detail', kwargs={'slug': post.slug})
        self.assertEqual(post.get_absolute_url(), expected_url)

    def test_is_featured_logic(self):
        first_post = Post.objects.create(
            title='First Featured', content='...', author=self.user, is_featured=True
        )
        self.assertTrue(first_post.is_featured)

        second_post = Post.objects.create(
            title='Second Featured', content='...', author=self.user, is_featured=True
        )

        first_post.refresh_from_db()
        self.assertFalse(first_post.is_featured)
        self.assertTrue(second_post.is_featured)


class PostImageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.com', password=password
        )
        self.category = Category.objects.create(name='TestCategory')
        self.post = Post.objects.create(
            title='Test Post Title',
            content='Some test content',
            author=self.user,
            category=self.category,
        )

    def test_postimage_creation(self):
        image_file = SimpleUploadedFile(
            'test_image.jpg', b'fake image content', content_type='image/jpeg'
        )

        post_image = PostImage.objects.create(post=self.post, image=image_file)

        self.assertEqual(post_image.post, self.post)
        self.assertTrue(post_image.image.name.startswith('post_images/'))
        self.assertIn(post_image, self.post.images.all())


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.user = User.objects.create_user(
            email='testuser@test.com', password=password
        )

    def test_category_creation_and_str(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(str(self.category), 'Test Category')

    def test_slug_is_generated(self):
        self.assertEqual(self.category.slug, slugify(self.category.name))

    def test_slug_is_unique(self):
        with self.assertRaises(Exception):
            Category.objects.create(name='Test Category')

    def test_post_count_method(self):
        self.assertEqual(self.category.post_count(), 0)

        Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            category=self.category,
        )
        self.assertEqual(self.category.post_count(), 1)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.com', password=password
        )
        self.category = Category.objects.create(name='TestCategory')
        self.post = Post.objects.create(
            title='Test Post Title',
            content='Some test content',
            author=self.user,
            category=self.category,
        )

    def test_comment_creation_and_str(self):
        comment = Comment.objects.create(
            post=self.post, user=self.user, text='This is a test comment.'
        )
        self.assertEqual(str(comment), f'Comment by {self.user} on {self.post}')
        self.assertFalse(comment.is_reply())

    def test_comment_reply_and_is_reply(self):
        parent_comment = Comment.objects.create(
            post=self.post, user=self.user, text='Parent comment'
        )
        reply = Comment.objects.create(
            post=self.post, user=self.user, text='Reply comment', parent=parent_comment
        )
        self.assertTrue(reply.is_reply())
        self.assertIn(reply, parent_comment.replies.all())

    def test_comment_ordering(self):
        c1 = Comment.objects.create(post=self.post, user=self.user, text='Old comment')
        c2 = Comment.objects.create(post=self.post, user=self.user, text='New comment')
        comments = list(Comment.objects.filter(post=self.post))
        self.assertEqual(comments[0], c2)
        self.assertEqual(comments[1], c1)
