# alx-backend-caching_property_listings

Django property listing app with Redis caching and Dockerized PostgreSQL & Redis.

## Quick start

1. Build and run containers:
   ```bash
   docker-compose up --build
   ```

2. Create a superuser (in another terminal):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

3. Visit http://localhost:8000/properties/ to see the property list.

## Notes

- View-level caching is applied to the property list view for 15 minutes.
- The property queryset is cached in Redis for 1 hour and invalidated on create/update/delete via Django signals.
- Redis cache metrics can be obtained with `properties.utils.get_redis_cache_metrics()`.
