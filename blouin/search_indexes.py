import datetime
from haystack import indexes
from blouin.models import Painting

class PaintingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    painter = indexes.CharField(model_attr='painter')
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Painting

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()