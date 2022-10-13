Create new posts
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample post list
----------------

.. code-block:: console

    User = get_user_model()

    Post.objects.create(
        author = User.objects.first(),
        title = "Test Post 1",
        body = "This is a test from the shell",
    )
    Post.objects.create(
        author = User.objects.get(username="susan"),
        title = "Test Post 2",
        body = "This is a second test from the shell",
    )
    Post.objects.create(
            author = User.objects.first(),
            title = "Django REST framework is a powerful toolkit",
            body = "Some reasons you might want to use REST framework:\r\n\r\n    The Web browsable API is a huge usability win for your developers.\r\n    Authentication policies including packages for OAuth1a and OAuth2.\r\n    Serialization that supports both ORM and non-ORM data sources.\r\n    Customizable all the way down - just use regular function-based views if you don't need the more powerful features.\r\n    Extensive documentation, and great community support.\r\n    Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.",
    )
    Post.objects.create(
            author = User.objects.get(username="john"),
            title = "Meet Django",
            body = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
    )
    Post.objects.create(
            author = User.objects.get(username="mary"),
            title = "Django is ridiculously fast",
            body = "Django was designed to help developers take applications from concept to completion as quickly as possible.",
    )
    Post.objects.create(
            author = User.objects.get(username="susan"),
            title = "Django is reassuringly secure",
            body = "Django takes security seriously and helps developers avoid many common security mistakes.",
    )
    Post.objects.create(
            author = User.objects.get(username="david"),
            title = "Django is exceedingly scalable",
            body = "Some of the busiest sites on the web leverage Django\u2019s ability to quickly and flexibly scale."
    )
    Post.objects.create(
            author = User.objects.get(username="alice"),
            title = "Civilization and its Discontents",
            body = "The real problem of humanity is the following: We have Paleolithic emotions, medieval institutions and godlike technology. And it is terrifically dangerous, and it is now approaching a point of crisis overall.",
    )
    Post.objects.create(
            author = User.objects.get(username="john"),
            title = "A painter's credo of service to State and Church",
            body = "And I have belief As I kneel now and light a candle, sensing A fitted silence in the weight of things. I am a man bound by indentures, agreements. All things dilate On the glory of empires, the prelates' zeal, The Saviour's great goodness in all His forms.",
    )
    Post.objects.create(
            author = User.objects.get(username="mary"),
            title = "Positivity",
            body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
    )
    Post.objects.create(
            author = User.objects.get(username="susan"),
            title = "Eric Dolphy",
            body = "Eric Dolphy was an American jazz alto saxophonist, bass clarinetist and flautist. Dolphy was one of several multi-instrumentalists to gain prominence in the same era. Dolphy extended the vocabulary and boundaries of the alto saxophone, and was among the earliest significant jazz flute soloists.",
    )
    Post.objects.create(
            author = User.objects.get(username="david"),
            title = "PEP 673: Self Type Was Accepted",
            body = "This PEP introduces a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach specified in PEP 484 but is more concise and easier to follow.",
    )
    Post.objects.create(
            author = User.objects.get(username="alice"),
            title = "Upcoming Python Feature PEPs",
            body = "These PEPs are a great way of getting the freshest info about what might be included in the upcoming Python releases. So, in this article we will go over all the proposals that are going to bring some exciting new Python features in a near future!",
    )
    Post.objects.create(
            author = User.objects.get(username="kbowen"),
            title = "Positivity",
            body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
    )
