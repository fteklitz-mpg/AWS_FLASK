friends = {'bob', 'bill', 'sid', 'jack'}
abroad = {'bob', 'sid'}

local_friends = friends.difference(abroad)
print(local_friends)

friends = {'bob', 'bill', 'sid'}
abroad = {'bob', 'sid'}
local_friends = abroad.difference(friends)
print(local_friends)
# produces empty set

local = {'bob', 'bill', 'sid'}
abroad = {'ed', 'ray'}
friends = local.union(abroad)
print(friends)
# produces empty set

art = {'bob', 'bill', 'sid'}
science = {'bob', 'bill', 'ed', 'ray'}
both = art.intersection(science)
print(both)