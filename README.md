django-never-cache-post
=======================

A simple middleware to work around a bug in iOS 6 that caches the results of
$.ajax POST requests inappropriately. (See ["Is Safari on iOS 6 caching $.ajax results?"](http://stackoverflow.com/q/12506897/400691) on Stack Overflow.)

This solution is inspired by [Meilo's answer to "Fighting client-side caching in Django"](http://stackoverflow.com/a/5882033/400691), also on Stack Overflow.

Installation
------------

Install from pypi.

    pip install django-never-cache-post

In your settings:

* Add `'never_cache_post'` to `INSTALLED_APPS`.
* Add `'never_cache_post.middleware.NeverCachePostMiddleware'` to `MIDDLEWARE_CLASSES`.
