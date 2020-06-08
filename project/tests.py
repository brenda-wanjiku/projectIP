from django.test import TestCase

# Create your tests here.
def setUp(self)
        ''' 
        creating a new user and saving it
        '''
        self.new_user = User(password='brownsugar',  email = "bs@gmail.com",password = "bswopqd")
        self.new_user.save()

        '''
        creating a new profile and saving it
        '''
        self.new_profile = Profile(profile_photo='photo.jpg', bio='Nice', contact='bw@gmail.com')
        self.new_profile.save()

        '''
        creating a new image and saving it
        '''
        self.new_project = Project(title='test', image='photo.jpeg',description='testing testing', link='http/github.com', profile=self.new_profile)
        self.new_project.save()

    def tearDown(self) -> None:
        Project.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.new_project, Project))
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))

    def test_save_project(self):
          '''
        Tests whether new image is added
        '''
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

   
    def test_delete_project(self):
         '''
        Tests whether new image is deleted
        ''' 
        self.new_project.save_project()
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
 
                
    def test_update_project_title(self):
         '''
        Tests whether the title is updated
        '''
        self.new_project.save_project()
        updated_project = Project.update_project_title(self.new_project.id, 'title2')
        self.assertEqual(updated_project.title, 'title2')

        
    def test_update_project_description(self):
        '''
        This tests whether project description is updated
        '''
        self.new_project.save_project()
        updated_project = Project.update_project_description(self.new_project.id, 'title2 description')
        self.assertEqual(updated_project.description, 'title2 description')

     def test_update_project_link(self):
        '''
        This tests whether project link is updated
        '''
        self.new_project.save_project()
        updated_project = Project.update_project_link(self.new_project.id, 'www.test2.com')
        self.assertEqual(updated_project.link, 'www.test2.com')

    def test_update_project_image(self):
        '''
        This tests whether project link is updated
        '''
        self.new_project.save_project()
        updated_project = Project.update_project_image(self.new_project.id, 'test2.jpg')
        self.assertTrue(updated_project.image != self.new_project.image)

    
class ProfileTestClass(TestCase):

    def setUp(self) 
        self.new_profile = Profile(profile_pic='photo.jpg', bio='Nice', contact='bw@gmail.com')

    def tearDown(self)
        Profile.objects.all().delete()

    def test_save_user_profile(self):
        self.new_profile.save_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_user_profile(self):
        self.new_profile.save_user_profile()
        self.new_profile.delete_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile_bio(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_bio(self.new_profile.id, 'Bad')
        self.assertEqual(updated_profile.bio, 'Bad')

    def test_update_profile_pic(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_pic(self.new_profile.id, 'gp.jpg')
        self.assertTrue(updated_profile.profile_pic != self.new_profile.profile_pic)


class RatingTestClass(TestCase):
    def setUp(self) 
     
        self.new_user = User(password='brownsugar',  email = "bs@gmail.com",password = "bswopqd")
        self.new_user.save()

        # creating a new profile and saving it
        self.new_profile = Profile(profile_photo='photo.jpg', bio='Nice', contact='bw@gmail.com')
        self.new_profile.save()

        # creating a new project and saving it
        self.new_project = Project(title='test', image='photo.jpeg',description='testing testing', link='http/github.com', profile=self.new_profile)
        self.new_project.save()

        # creating a new rating for project and saving it
        self.new_rating = Rating(design=4, usability=7, content=4, project=self.new_project, user=self.new_user)
        self.new_rating.save()

    def tearDown(self) -> None:
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_project, Project))
        self.assertTrue(isinstance(self.new_rating, Rating))

    def test_save_rating(self):
        self.new_rating.save_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) > 0)

    def test_delete_rating(self):
        self.new_rating.save_rating()
        self.new_rating.delete_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) == 0)

    def test_update_design_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_design_rating(self.new_project, 8)
        self.assertEqual(updated_rating.design, 8)

    def test_update_usability_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_usability_rating(self.new_project, 9)
        self.assertEqual(updated_rating.usability, 9)

    def test_update_content_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_content_rating(self.new_project, 6)
        self.assertEqual(updated_rating.content, 6)