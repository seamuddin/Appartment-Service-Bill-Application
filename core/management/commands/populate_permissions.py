from django.core.management.base import BaseCommand
from django.urls import get_resolver, resolve
from core.models import CustomPermission
from django.urls import URLPattern, URLResolver
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate custom permissions'

    def handle(self, *args, **options):
        # Get the root URL resolver
        root_urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
        url_patterns = root_urlconf.urlpatterns
        import pdb;
        pdb.set_trace()

        # Iterate over all the URLs in the project
        for pattern in url_patterns:
            self.process_pattern(pattern, '')

    def process_pattern(self, pattern, namespace):
        if isinstance(pattern, URLPattern):
            # If the pattern is a URL pattern, add a custom permission for the URL
            name = self.get_name_for_pattern(pattern, namespace)
            url = self.get_url_for_pattern(pattern, namespace)
            import pdb; pdb.set_trace()
            print(url)
            CustomPermission.objects.create(name=name, url=url)
        elif isinstance(pattern, URLResolver):
            # If the pattern is a URL resolver, recurse over its patterns with the correct namespace
            if pattern.namespace:
                namespace = f'{namespace}:{pattern.namespace}'
            self.process_pattern(pattern.url_patterns, namespace)

    def get_name_for_pattern(self, pattern, namespace):
        # Generate a name for the permission based on the view name and namespace
        name = pattern.callback.__name__
        if namespace:
            name = f'{namespace}:{name}'
        return name

    def get_url_for_pattern(self, pattern, namespace):
        # Generate the full URL for the pattern
        if namespace:
            return f'/{namespace}/{pattern.pattern}'
        else:
            return f'/{pattern.pattern}'