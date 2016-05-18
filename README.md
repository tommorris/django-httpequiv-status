django-httpequiv-status
=======================

Very basic Django middleware implementation of
[meta-httpequiv-status](https://indiewebcamp.com/meta_http-equiv_status).

Warning #1: likely to be very slow. You probably want to cache the result of
this. Or, better yet, build your app in such a way that it isn't necessary.

Warning #2: the code for Django's streaming support is completely untested.
Bug reports welcome.