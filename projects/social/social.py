import random 
# from collections import defaultdict


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.num_friendships = 0
        self.friendships = {}


    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            self.num_friendships += 1


    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.last_id += 1  # automatically increment the ID to assign the new user

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        if num_users < avg_friendships:
            print('ERROR: Number of users must be greater than the average number of friendships.')
            return 

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.num_friendships = 0
        self.friendships = {}

        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'u{i}')

        # Create friendships
        friendships_all = []
        for i in range(0, num_users):
            for j in range(i+1, num_users):
                friendships_all.append([i, j])
        self.num_friendships = num_users * avg_friendships // 2
        for user_id, friend_id in random.sample(friendships_all, self.num_friendships):
            self.add_friendship(user_id, friend_id)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # bfs/bft
        paths = [[user_id]]
        while paths:
            path = paths.pop(0)
            friend_id = path[-1]
            if friend_id not in self.friendships:
                continue
            friendships = self.friendships[friend_id]
            for friendship in friendships:
                if friendship in visited or friendship == user_id:
                    continue
                path_new = path.copy()
                path_new.append(friendship)
                paths.append(path_new)
                visited[friendship] = path_new

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'friendships: {sg.friendships}')

    for user_id in sg.users:
        connections = sg.get_all_social_paths(user_id)
        print(f'user {user_id}\'s connections: {connections}')