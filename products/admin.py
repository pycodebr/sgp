import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="brands.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for brand in queryset:
            writer.writerow([brand.name, brand.is_active, brand.description,
                             brand.created_at, brand.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="categories.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for category in queryset:
            writer.writerow([category.name, category.is_active, category.description,
                             category.created_at, category.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price',
                    'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'brand__name', 'category__name')
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
