import random
from instapy import InstaPy
from instapy.util import smart_run

# get a session!
session = InstaPy(username='', password='',  proxy_address=0,
                  proxy_port=3128, headless_browser=True)

# let's go! :>
with smart_run(session):
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelingcouple',
                'backpackerlife', 'travelguide', 'travelbloggers',
                'travelblog', 'letsgoeverywhere',
                'travelislife', 'stayandwander', 'beautifuldestinations',
                'moodygrams',
                'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
                'lonelyplanet',
                'igtravel', 'instapassport', 'travelling', 'instatraveling',
                'travelingram',
                'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'travelblog',
                'sunset_pics', 'visiting', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'landscapeporn', 'exploring_shotz',
                'landscapehunter', 'colors_of_day',
                'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'thegreatoutdoors']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=40, times=1)
    session.set_do_comment(enabled=True, percentage=30)
    session.set_comments([
                             u'What an amazing shot! :heart_eyes: What do '
                             u'you think of my recent shot?',
                             u'What an amazing shot! :heart_eyes: I think '
                             u'you might also like mine. :wink:',
                             u'Wonderful!! :heart_eyes: Would be awesome if '
                             u'you would checkout my photos as well!',
                             u'Wonderful!! :heart_eyes: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'This is awesome!! :heart_eyes: Any feedback '
                             u'for my photos? :wink:',
                             u'This is awesome!! :heart_eyes:  maybe you '
                             u'like my photos, too? :wink:',
                             u'I really like the way you captured this. I '
                             u'bet you like my photos, too :wink:',
                             u'I really like the way you captured this. If '
                             u'you have time, check out my photos, too. I '
                             u'bet you will like them. :wink:',
                             u'Great capture!! :smiley: Any feedback for my '
                             u'recent shot? :wink:',
                             u'Great capture!! :smiley: :thumbsup: What do '
                             u'you think of my recent photo?'],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max=100, min=0)
    session.set_delimit_commenting(enabled=True, max=20, min=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=100,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes=(100, 1000),
                                 peak_comments=(21, 250),
                                 peak_follows=(200, None))

    session.set_user_interact(amount=1, randomize=False, percentage=40)

    # activity
    session.like_by_tags(my_hashtags, amount=60, media=None)
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)
