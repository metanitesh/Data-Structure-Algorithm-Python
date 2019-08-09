class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group, output= False):

  if user in group.users:
    return 'True'
  for gr in group.groups:
    output = is_user_in_group(user, gr)
  return output

#Test-1
parent = Group("parnet")
parent_user = "parent_user"
parent.add_user(parent_user)
print(is_user_in_group('parent_user', parent))
# True

#Test-2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user', parent))
# True


#Test-3
parent = Group("parent")
print(is_user_in_group('no_child', parent))
# False



