from django.views.generic.list import ListView
from django.db.models import Q, Count

from . import models


class GroupListView(ListView):
    model = models.Group
    
    queryset = (
        models.Group.objects
        .annotate(
            things = Count('item', filter = Q(item__type = models.Item.Type.THING)),
        )
    )

