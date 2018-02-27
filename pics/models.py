from django.db import models

# creating  models

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id=id).update(location=update)
        return updated        

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
      self.save()

    
    def delete_category(self):
        self.delete()
class Image(models.Model):
    name = models.CharField(max_length =30)
    description =  models.CharField(max_length =30)
    location = models.ForeignKey(Location,null =True)
    category = models.ForeignKey(Category,null = True)
    image = models.ImageField(upload_to = 'image/',null = True)
    # upload_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'category/',null=True,blank=True)

    def __str__(self):
       return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
      self.remove()

    @classmethod
    def update_image(cls, id, update):
        updated = cls.objects.filter(id=id).update()
        return updated

    @classmethod
    def get_image(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def get_all(cls):
        images = cls.objects.all('-category')
        return images

    @classmethod
    def searched(cls,query):
        result = cls.objects.filter(category__name__icontains=query)
        return result    

    @classmethod
    def filter_by_location(cls,id):
        images = Image.objects.filter(id=location.id)
        return images   
