from django.shortcuts import render
from .models import Photo, Topic
from django.core.paginator import Paginator

image_column_number = 5


def index(request):
    topics = Topic.objects.all().order_by('-date')

    paginator = Paginator(topics,8)
    page = request.GET.get('page')
    topics = paginator.get_page(page)


    images = []
    
    for t in topics:
        images.append(t.photo_set.first())

    topics_and_images = zip(topics, images)
    #print(topics[5].photo_set.all())
    return render(request, 'gallery/index.html', {'topics_and_images': topics_and_images, 'topics': topics})


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    images = Topic.objects.get(id=topic_id).photo_set.all()
 
    return render(request, 'gallery/topic.html', {'topic': topic, 'images': images})
