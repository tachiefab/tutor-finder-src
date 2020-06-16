from django.contrib import admin
from .models import ObjectViewed

class ObjectViewedAdmin(admin.ModelAdmin):
	list_display = ["__str__", "content_object", "content_type", "user", "ip_address", "timestamp", "count"]
	search_fields = ["user", "ip_address"]
	list_filter = ["user", "content_type", "ip_address"]

	class Meta:
		model = ObjectViewed

admin.site.register(ObjectViewed, ObjectViewedAdmin)