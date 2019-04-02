from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project= Profile(title = 'Project', image ='photo', bio ='information')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.project.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.title = Project(image = 'photo', description ='text', link ='url')


    # Creating a new tag and saving it
        self.new_project = projects(title = 'testing')
        self.new_project.save()

        self.new_project= Project(title = 'Test Project',post = 'This is a random test Post',profile = self.title)
        self.new_project.save()

        self.new_project.projects.add(self.new_project)

    def tearDown(self):
        Profile.objects.all().delete()
        projects.objects.all().delete()
        Project.objects.all().delete()


