from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username')
    #search_fields = ('title','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        res = ""
        for c in obj.categories.all().order_by("name"):
            res += c.name + ", "
        res = res[0:len(res)-2]
        return res
        # return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Category, CategoryAdmin)
