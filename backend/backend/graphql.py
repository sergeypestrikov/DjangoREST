import graphene
from graphene_django import DjangoObjectType

from user_app.models import User
from TODO_app.models import Project, Task


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TaskObjectType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class Query(graphene.ObjectType):

    # hello = graphene.String()
    #
    # def resolve_hello(self, info):
    #     return 'world!'

    all_users = graphene.List(UserObjectType)

    def resolve_all_users(self, info):
        return User.objects.all()


    all_projects = graphene.List(ProjectObjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()


    all_tasks = graphene.List(TaskObjectType)

    def resolve_all_tasks(self, info):
        return Task.objects.all()


    get_user_by_id = graphene.Field(UserObjectType, pk=graphene.Int(required=True))

    def resolve_get_user_by_id(self, info, pk):
        return User.objects.get(pk=pk)

    get_user_by_name = graphene.Field(UserObjectType,
                                      username=graphene.String(required=False),
                                      name=graphene.String(required=False)
                                      )

    def resolve_get_user_by_name(self, info, username=None, name=None):
        if not username and not name:
            return User.objects.all()
        params = {}
        if name:
            params['name__contains'] = name
        if username:
            params['username__contains'] = username
        return User.objects.filter(**params)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        username = graphene.String(required=True)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, name, username):
        user = User(name=name, username=username)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        username = graphene.String(required=False)
        name = graphene.String(required=False)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, pk, username=None, name=None):
        user = User.objects.get(pk=pk)
        if name:
            user.name = name
        if username:
            user.username = username

        if name or username:
            user.save()
        return cls(user)


class Mutations(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)