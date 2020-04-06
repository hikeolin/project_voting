

'''
    vote class consumers
'''
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db import models
from api.models import Poll, VoteLogs
import json
import urllib.parse as urlparse 

class PollVoteConsumer(WebsocketConsumer):

    def connect(self):
        try:
            self.poll_uid = self.scope['url_route']['kwargs']['poll_uid']
            params = urlparse.parse_qs(self.scope['query_string'])
            self.user_id = params.get(b'u_uid', (None))[0]
            if self.user_id is not None:
                self.user_id = self.user_id.decode()
            async_to_sync(self.channel_layer.group_add)(
                'poll_%s' % self.poll_uid,
                self.channel_name)
            self.accept()
        except Exception as e:
            print(e)
            self.close()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
             'poll_%s' % self.poll_uid,
            self.channel_name)

    def receive(self, text_data):
        content = json.loads(text_data)
        msg = content['candidate_uid']
        async_to_sync(self.channel_layer.group_send)(
            'poll_%s' % self.poll_uid,
            {
                'type': 'vote.candidate',
                'uid': msg
            }
        )
        
    def vote_candidate(self, event):
        uid = event['uid']
        print('candidate uid => %s' % uid)
        has_voted = VoteLogs.objects.filter(poll_id=self.poll_uid, user_id=self.user_id).exists()
        if not has_voted:    
            self.update_vote_history(uid, self.poll_uid)
            self.add_to_logs(self.user_id, self.poll_uid)
            self.send(text_data=json.dumps({
                'tvotes': poll.tvotes
            }))

        else:
            self.send(text_data=json.dumps({
                'error': 'user with %s already voted' % self.user_id                
            }))
    
    def update_vote_history(self, uid, pool_uid):
        # get poll object and candidate object
        poll = Poll.objects.get(pk=self.poll_uid)
        candidate = poll.candidate_set.get(pk=uid)
        # update candidate vote count 
        candidate.votes = candidate.votes + 1
        candidate.save() # save changes of course :)
        poll.tvotes = poll.candidate_set.aggregate(models.Sum('votes'))['votes_sum']
        poll.save()  # save changes
    
    def add_to_logs(self, user_id, poll_uid):
        new_log = VoteLogs.objects.create(user_id=user_id, poll_id=poll_uid)
        new_log.save()