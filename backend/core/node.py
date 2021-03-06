from graphene.relay import Node as _Node

DIVIDER = "@"


class Node(_Node):
    @staticmethod
    def gid2id(gid):
        return Node.from_global_id(gid)[1]

    @staticmethod
    def from_global_id(gid):
        return gid.split(DIVIDER, 1)

    @staticmethod
    def to_global_id(type, id):
        return f"{type}{DIVIDER}{id}"
