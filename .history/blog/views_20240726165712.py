from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Arda",
        "date": date(2024,7,26),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking in the mountains. And I wasn't even prepared for what happened whilst I was enjoying the view.",
        "content": """Cum consectetur nihil, aut quam pariatur asperiores. Laborum reprehenderit 
        deserunt saepe suscipit, officiis neque repellendus esse doloribus quibusdam quasi, quo quis doloribus 
        eaque unde saepe laboriosam officia? Illo magnam consectetur qui ipsum esse similique sit dolore aliquid? 
        Impedit maxime iusto soluta ab vero minus cum ad. Labore officiis alias quis aspernatur, tempore facilis error nulla magni 
        maiores sunt nostrum architecto voluptates vel? 
        Eveniet cum provident ipsum laboriosam suscipit repellendus eos facilis, laudantium fugit temporibus aut neque perspiciatis officia animi optio voluptates eaque? Enim voluptatibus obcaecati aliquid reiciendis cum amet illo quidem dolorem nihil 
        fugit, non nihil asperiores beatae eaque at dolore voluptatibus culpa incidunt. 
        Incidunt sint soluta sit vero laboriosam sed, obcaecati magnam in reprehenderit nobis necessitatibus temporibus, consectetur cumque 
        voluptatibus praesentium facilis atque distinctio rerum consequatur libero? Nobis sequi odio facilis ut consequatur autem rem sed, rerum aut obcaecati possimus perspiciatis culpa quaerat ex architecto autem molestias labore, laborum ex fugiat voluptate aperiam, rerum nobis dolores harum ipsam tempora commodi. Tempore ducimus corporis quia exercitationem dolorem facilis eveniet, nostrum explicabo facere fugiat eum sequi laboriosam minima soluta iste at, animi veniam consequatur eius dolore placeat soluta dicta facere amet error."""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']

def get_single_post

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key= get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request, slug):
    return render(request, "blog/post-detail.html",{
        "post": all_posts[slug]
    })


    
