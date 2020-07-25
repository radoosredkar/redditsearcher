import graphene
from models import SubRedditModel
from graphene_sqlalchemy import SQLAlchemyObjectType


class SubReddit(SQLAlchemyObjectType):
    class Meta:
        model = SubRedditModel


class Query(graphene.ObjectType):
    subreddits = graphene.List(SubReddit)
    subreddit = graphene.List(
        SubReddit,
        title=graphene.String(),
        desc=graphene.String(),
        flair=graphene.String(),
    )

    def resolve_subreddits(self, info):
        query = SubReddit.get_query(info)
        return query.all()

    def resolve_subreddit(self, info, **args):
        ident = args.get("ident")
        title = args.get("title")
        description = args.get("desc")
        flair = args.get("flair")

        flt = []
        if title:
            flt.append((SubRedditModel.title.contains(title)))
        if description:
            flt.append((SubRedditModel.description.contains(description)))
        if flair:
            flt.append((SubRedditModel.flair.contains(flair)))

        query = SubReddit.get_query(info)
        if ident:
            return query.get(ident)
        else:
            sql = query.filter(*flt)
            print(sql)
            return sql.all()


schema = graphene.Schema(query=Query)
