from django.shortcuts import render


posts = [
    {
        'author': 'Dennis Akagha',
        'title': 'This is for developers',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium omnis odio adipisci numquam harum necessitatibus, voluptatum vel veniam tempora assumenda.',
        'dateCreated': '12th, March 2020',
    },
     {
        'author': 'Peter Joel',
        'title': 'Learn Django in three days',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium omnis odio adipisci numquam harum necessitatibus, voluptatum vel veniam tempora assumenda.',
        'dateCreated': '15th, March 2022',
    },
     {
        'author': 'Okechukw Daniel',
        'title': 'Learn HTML',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium omnis odio adipisci numquam harum necessitatibus, voluptatum vel veniam tempora assumenda.',
        'dateCreated': '15th, March 2022',
    }
]



def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)
