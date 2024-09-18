import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ads.models import Advert, Category


class AdvertType(DjangoObjectType):
    class Meta:
        model = Advert
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = "id", 'name'
        interfaces = relay.Node,


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(
            name=name
        )
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name):
        category = Category.objects.get(pk=id)
        category.name = name if name is not None else category.name
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return DeleteCategory(category=category)


class Query(graphene.ObjectType):
    adverts = graphene.List(AdvertType)
    # categories = graphene.List(CategoryType, description='Bu kategoriya hisoblanadi')
    # category = graphene.Field(CategoryType, id=graphene.ID())
    category = relay.Node.Field(CategoryType)
    categories = DjangoFilterConnectionField(CategoryType, limit=graphene.Int())

    def resolve_categories(self, info, **kwargs):
        qs = Category.objects.all()
        offset = kwargs.get('offset')
        limit = kwargs.get('limit')
        if offset and limit:
            qs = qs[offset:offset + limit]
        return qs

    def resolve_category(self, info, id):
        return Category.objects.get(pk=id)

    def resolve_all_adverts(self, info):
        return Advert.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
