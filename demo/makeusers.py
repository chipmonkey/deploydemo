import demo
import names

NUMUSERS=100

for i in range(NUMUSERS):
    user = demo.models.User(name=names.get_full_name())
    demo.db.session.add(user)

demo.db.session.commit()
