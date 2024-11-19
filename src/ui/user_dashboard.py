from tkinter import Frame, Radiobutton, ttk, StringVar, Listbox
from services.user_service import UserService
from services.group_service import GroupService

class UserDashboard:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(master=self.root)

        # Alustetaan palvelut käyttäjille ja ryhmille
        self.group_service = GroupService()
        self.user_service = UserService(self.group_service)

        # Käyttäjän luontialue
        self.user_name_var = StringVar()
        self.user_role_var = StringVar()
        self.user_group_var = StringVar()

        ttk.Label(self.frame, text="Create User").pack()

        # Nimilappu ja syöttökenttä käyttäjän nimelle
        ttk.Label(self.frame, text="Username:").pack(anchor="w") 
        ttk.Entry(self.frame, textvariable=self.user_name_var).pack()

        # Roolin valinta radiopainikkeilla
        ttk.Label(self.frame, text="Role:").pack(anchor="w")
        role_frame = Frame(self.frame)
        role_frame.pack(anchor="w")
        
        # Luodaan roolin valintapainikkeet
        Radiobutton(role_frame, text="Ryhmänjohtaja", variable=self.user_role_var, value="Ryhmänjohtaja").pack(side="left")
        Radiobutton(role_frame, text="Admin", variable=self.user_role_var, value="Admin").pack(side="left")

        ttk.Label(self.frame, text="Group:").pack(anchor="w")
        self.user_group_combobox = ttk.Combobox(self.frame, textvariable=self.user_group_var)
        self.user_group_combobox.pack()
        self.update_group_combobox()  # Täytetään valikko alussa

        ttk.Button(self.frame, text="Add User", command=self.create_user).pack()

        # Ryhmän luontialue
        self.group_name_var = StringVar()

        ttk.Label(self.frame, text="Create Group").pack()
        ttk.Label(self.frame, text="Group Name:").pack(anchor="w")
        ttk.Entry(self.frame, textvariable=self.group_name_var).pack()
        ttk.Button(self.frame, text="Add Group", command=self.create_group).pack()

        # Käyttäjän lisääminen/poistaminen ryhmästä
        self.modify_user_name_var = StringVar()
        self.modify_group_name_var = StringVar()

        ttk.Label(self.frame, text="Modify Group Membership").pack()
        ttk.Label(self.frame, text="Username:").pack(anchor="w")
        ttk.Entry(self.frame, textvariable=self.modify_user_name_var).pack()
        ttk.Label(self.frame, text="Group Name:").pack(anchor="w")
        ttk.Entry(self.frame, textvariable=self.modify_group_name_var).pack()
        ttk.Button(self.frame, text="Add to Group", command=self.add_user_to_group).pack()
        ttk.Button(self.frame, text="Remove from Group", command=self.remove_user_from_group).pack()

        # Käyttäjälista
        ttk.Label(self.frame, text="Users").pack()
        self.user_listbox = Listbox(self.frame)
        self.user_listbox.pack()

        # Ryhmälista
        ttk.Label(self.frame, text="Groups").pack()
        self.group_listbox = Listbox(self.frame)
        self.group_listbox.pack()

        self.frame.pack()


    def create_user(self):
        username = self.user_name_var.get()
        role = self.user_role_var.get()
        group = self.user_group_var.get()
        # Need to add checks if the group exists
        self.user_service.add_user(username, role, group)
        self.update_user_list()
        self.update_group_list()

    def create_group(self):
        group_name = self.group_name_var.get()
        # Need to add checks if the group exists
        self.group_service.create_group(group_name)
        self.update_group_list()
        self.update_group_combobox()

    def add_user_to_group(self):
        username = self.modify_user_name_var.get()
        group_name = self.modify_group_name_var.get()
        user = next((u for u in self.user_service.list_users() if u.username == username), None)
        group = next((g for g in self.group_service.list_groups() if g.name == group_name), None)
        if user and group:
            group.add_participant(user)
            self.update_group_list()
            self.update_user_list()

    def remove_user_from_group(self):
        username = self.modify_user_name_var.get()
        group_name = self.modify_group_name_var.get()
        user = next((u for u in self.user_service.list_users() if u.username == username), None)
        group = next((g for g in self.group_service.list_groups() if g.name == group_name), None)
        if user and group:
            group.remove_user_from_list(user, group.participants)
            self.update_group_list()
            self.update_user_list()

#Tämä metodi luotu tekoälyn avulla
    def update_user_list(self):
        self.user_listbox.delete(0, 'end')
        for user in self.user_service.list_users():
            self.user_listbox.insert('end', f"{user.username} ({user.role}) - Group: {user.group}")

    def update_group_list(self):
        self.group_listbox.delete(0, 'end')
        for group in self.group_service.list_groups():
            participants = ", ".join([p.username for p in group.participants])
            self.group_listbox.insert('end', f"{group.name} - ({group.calendars}) - Participants: {participants}")

    def update_group_combobox(self):
      # Päivittää Comboboxin vaihtoehdot nykyisten ryhmien nimillä
        group_names = [group.name for group in self.group_service.list_groups()]
        self.user_group_combobox['values'] = group_names

    def destroy(self):
        self.frame.destroy()