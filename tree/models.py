from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class TestTree(MPTTModel):
# class TestTree(models.Model):
    name = models.CharField(max_length=128)
    # Added after the creation of model, made - 
    # the migration and added data to the db.
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(TestTree, self).save(*args, **kwargs)
        try:
            trees = TestTree.objects.all()
            for tree in trees:
                if tree.lft or tree.rght or tree.tree_id == 0:
                    TestTree.objects.rebuild()

        except Exception as e:
            print(e)
            pass
