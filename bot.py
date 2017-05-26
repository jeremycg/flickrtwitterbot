import flickrapi
from twython import Twython
import random
import urllib.request as ur
import json

key = '#'
secret = '#'

flickr = flickrapi.FlickrAPI(key,secret, format = 'json')

twitter = Twython("#",
                  "#",
                  "#",
                  "#")


photos = json.loads(flickr.photos.search(
        tag_mode = 'all',
        tags='kitten,cute',
        license = '4,5,6,7,8',
        safe_search = 1,
        per_page = 200,
        extras = 'owner_name'
).decode('utf-8'))

tweeted = 0
while tweeted == 0:
    try:
        photo = random.choice(photos['photos']['photo'])
        tweet = '"{title}" by {ownername} posted at http://flickr.com/photos/{owner}/{ids}'.format(title = photo['title'],\
            ownername = photo['ownername'], owner = photo['owner'], ids = photo['id'])
        print(tweet)
        f = open('totweet.jpg','wb')
        f.write(ur.urlopen('http://farm{farm}.staticflickr.com/{server}/{ids}_{secret}_z.jpg'.format(farm = photo['farm'],\
            server = photo['server'], ids = photo['id'], secret = photo['secret'])).read())
        f.close()
        pic = open('totweet.jpg', 'rb')
        response = twitter.upload_media(media=pic)
        twitter.update_status(status=tweet, media_ids=[response['media_id']])
        tweeted = 1
    except Exception as e:
        print(e)
        pass
