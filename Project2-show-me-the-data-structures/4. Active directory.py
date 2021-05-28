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
    
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    # First check whether group is valid
    try:
        group.get_groups()
    except:           
        return ('Invalid group')
    
    # Now recursively check whether user exist in group
    
    if user in group.get_users():
        return True   # user in group
    else:
        # Search recursively..
        if len(group.get_groups()) == 0:
            return False
        else:
            for inner_group in group.get_groups():
                if is_user_in_group(user, inner_group):                     
                    return True                 
                    
    
        return False


# Testing..
# First Generate some relationships of groupds and users

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test case 1
print(is_user_in_group(user = 'sub_child_user', group = parent))
# True

# Test case 2
print(is_user_in_group(user = 'child', group = child))
# False

# Test case 3
print(is_user_in_group(user = 'sub_user', group = child))
# False

# Test case 4 (Edge Case)
print(is_user_in_group(user = '', group = parent))
# False

# Test case 5 (Edge Case)
print(is_user_in_group(user = '', group = ''))
# Invalid group