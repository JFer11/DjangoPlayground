from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # Important to highlight, inside a manager, self is equal to <Model>.objects.all()
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

    objects = ThreadManager()


def messages_changed(sender, **kwargs):
    instance = kwargs.pop('instance')
    action = kwargs.pop('action')
    pk_set = kwargs.pop('pk_set')

    false_pk_set = set()
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                # We do not allow to register the message, because the user is not part of the thread.
                # Python detail: It is forbidden to change a set during an iteration (pk_set.remove(msg_pk))
                false_pk_set.add(msg_pk)

    pk_set.difference_update(false_pk_set)


m2m_changed.connect(messages_changed, Thread.messages.through)
