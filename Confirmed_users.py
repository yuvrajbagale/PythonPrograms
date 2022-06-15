unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())