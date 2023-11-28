####################################
#       SaveTheEnvironment.exe     #
#         Author: Jan Munro        #
#      Start Date: 23/08/2023      #
#       End Date: 03/11/2023       #
####################################

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from random import randint


def new_windows(window: str,
                window_width: int = 400,
                window_height: int = 400) -> None:

    root = tk.Tk()
    root.title("")

    if window == "Login":
        gui_window = LoginGUI(root)
    elif window == "Signup":
        gui_window = SignupGUI(root)
    else:
        # root.title("SaveTheEnvironment.exe")
        if window == "Tasks":
            root.title("Tasks")
            gui_window = TasksGUI(root)
        elif window == "Shop":
            root.title("Shop")
            gui_window = ShopGUI(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    root.mainloop()


class Task:

    def __init__(
            self, info: list[any]
            ) -> None:
        self.name: str = info[0]
        self.image: str = info[1]
        self.threshold: int = info[2]
        self.value: int = info[3]


class Item:

    def __init__(
            self, name: str, image: str, price: int  # , description: str
            ) -> None:
        self.name = name
        self.image = image
        self.price = price
        # self.description = description

    def test(self) -> None:
        self.name = "Test Item"
        self.description = f"Test Code: {randint(0, 999999)}"
        self.price = randint(0, 100)


class Order:

    def __init__(self, name: str, contents: list[Item]) -> None:
        self.name = name
        self.contents = contents
        self.total: int = 0
        for item in contents:
            self.total += item.price


class User:

    def __init__(self, info: list[any]) -> None:
        self.name = info[0]
        self.password = info[1]
        self.mail = info[2]
        self.balance: int = 0 if len(info) < 4 else info[3]
        self.tasks: dict[Task, int] = {} if len(info) < 5 else info[4]
        self.cart: list[Item] = [] if len(info) < 6 else info[5]
        self.orders: list[Order] = [] if len(info) < 7 else info[6]
        self.active: bool = False

    def update_task(self, task: Task):
        if task in self.tasks:
            if self.tasks[task] == task.threshold - 1:
                self.tasks[task] = 0
                self.balance += task.value
            else:
                self.tasks[task] += 1
        else:
            self.tasks[task] = 1

    def finalise_order(self):
        self.orders.append(Order(self.name, self.cart))


class LoginGUI:
    """
    Login screen.
    """

    def __init__(self, parent: tk.Tk) -> None:
        self.parent = parent
        parent.grid_columnconfigure(0, weight=1)

        image = tk.PhotoImage(file="hellyeah.png")
        background = tk.Label(parent, image=image)
        background.bg = image
        background.grid(row=0, rowspan=50)

        title = ttk.Label(
            parent,
            text="SaveTheEnvironment.exe",
            font=("Futura Bold", 20)
            )
        title.grid(row=0)

        self.username_entry = ttk.Entry(
            parent,
            textvariable=tk.StringVar,
            width=20,
            foreground="grey"
        )
        self.username_entry.grid(row=1)
        self.username_entry.insert(tk.END, "Username")
        self.username_entry.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.username_entry)
        )

        self.password_entry = ttk.Entry(
            parent,
            textvariable=tk.StringVar,
            width=20,
            foreground="grey"
        )
        self.password_entry.grid(row=2)
        self.password_entry.insert(tk.END, "Password")
        self.password_entry.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.password_entry)
        )

        login_button = ttk.Button(parent, text="Login...", command=self.login)
        login_button.grid(row=3)

        self.signup_button = ttk.Button(
            parent,
            text="Create new account?",
            command=self.goto_signup
        )
        self.signup_button.grid(row=4)

        parent.bind("<Key>", self.event_handler)

    def event_handler(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            self.parent.destroy()

    def clear_entry(self, entry_box: ttk.Entry) -> None:
        entry_box.delete(0, tk.END)
        if entry_box == self.password_entry:
            entry_box.configure(show="•")
        entry_box.configure(foreground="black")

    def login(self) -> None:
        for user in user_list:
            if user.name == self.username_entry.get():
                if user.password == self.password_entry.get():
                    user.active = True
                    self.parent.destroy()
                    new_windows("Tasks")
                else:
                    messagebox.showinfo(
                        "Incorrect Password.",
                        "Password doesn't match username.",
                        master=self.parent
                    )
            else:
                messagebox.showinfo(
                    "No User",
                    "No user exists with that account name.",
                    master=self.parent
                )
        else:
            messagebox.showinfo(
                "No Users",
                "No users have signed up yet.",
                master=self.parent
            )

    def goto_signup(self) -> None:
        self.parent.destroy()
        new_windows("Signup")


class SignupGUI:
    """
    Signup screen.
    """

    def __init__(self, parent: tk.Tk) -> None:
        self.parent = parent
        parent.grid_columnconfigure(0, weight=1)

        image = tk.PhotoImage(file="hellyeah.png")
        background = tk.Label(parent, image=image)
        background.bg = image
        background.grid(row=0, rowspan=50)

        title = ttk.Label(
            parent,
            text="SaveTheEnvironment.exe",
            font=("Futura Bold", 20)
            )
        title.grid(row=0)

        var1 = tk.StringVar
        self.username_entry = ttk.Entry(
            parent,
            textvariable=var1,
            width=20,
            foreground="grey"
        )
        self.username_entry.grid(row=1)
        self.username_entry.insert(tk.END, "Username")
        self.username_entry.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.username_entry)
        )

        var2 = tk.StringVar
        self.email_entry = ttk.Entry(
            parent,
            textvariable=var2,
            width=20,
            foreground="grey"
        )
        self.email_entry.grid(row=2)
        self.email_entry.insert(tk.END, "E-mail Address")
        self.email_entry.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.email_entry)
        )

        var3 = tk.StringVar
        self.password_entry = ttk.Entry(
            parent,
            textvariable=var3,
            width=20,
            foreground="grey"
        )
        self.password_entry.grid(row=3)
        self.password_entry.insert(tk.END, "Password")
        self.password_entry.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.password_entry)
        )

        var4 = tk.StringVar
        self.password_confirm = ttk.Entry(
            parent,
            textvariable=var4,
            width=20,
            foreground="grey"
        )
        self.password_confirm.grid(row=4)
        self.password_confirm.insert(tk.END, "Confirm Password")
        self.password_confirm.bind(
            "<Button-1>",
            lambda x: self.clear_entry(self.password_confirm)
        )

        self.error_text = ttk.Label(
            parent,
            text="Invalid details",
            foreground="red"
        )

        self.signup_button = ttk.Button(
            parent,
            text="Go!",
            command=self.signup_complete
        )
        self.signup_button.grid(row=6)

        self.login_button = ttk.Button(
            parent,
            text="Already have an account?",
            command=self.goto_login
        )
        self.login_button.grid(row=7)

        parent.bind("<Key>", self.event_handler)

    def event_handler(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            self.parent.destroy()

    def clear_entry(self, entry_box: ttk.Entry) -> None:
        entry_box.delete(0, tk.END)
        if entry_box == self.password_entry or \
                entry_box == self.password_confirm:
            entry_box.configure(show="•")
        entry_box.configure(foreground="black")

    def signup_complete(self) -> None:
        valid_email: bool = True
        if self.email_entry.get().count("@") == 1 and\
                ".." not in self.email_entry.get():
            address_domain = self.email_entry.get().split("@")
            for string in address_domain[1].split("."):
                if valid_email:
                    print(string)
                    if len(string) <= 1:
                        self.error_text.grid(row=5)
        else:
            self.error_text.grid(row=5)

        if self.username_entry.get() != "Username" and valid_email:
            if self.password_entry.get() == self.password_confirm.get():
                user_list.append(User([
                    self.username_entry.get(),
                    self.password_entry.get(),
                    self.email_entry.get()
                ]))
                user_list[-1].active = True
                self.parent.destroy()
                new_windows("Tasks")
            else:
                self.error_text.grid(row=5)
        else:
            self.error_text.grid(row=5)

    def goto_login(self) -> None:
        self.parent.destroy()
        new_windows("Login")


def create_task_element(
            parent: tk.Tk, file: str,
            title: str,  # description: str
            ) -> ttk.Frame:
    box = ttk.Frame(parent)

    title_label = ttk.Label(box, text=title, font=("Futura", 10, "bold"))
    title_label.pack()

    img = ImageTk.PhotoImage(
        Image.open(file).resize((100, 100), Image.LANCZOS), master=box
    )
    image_label = ttk.Label(box, image=img)
    image_label.image = img
    image_label.pack()

    # description_label = ttk.Label(
    #     box, text=description, font=("Futura", 15)
    # )
    # description_label.pack()

    return box


def create_shop_item(
            parent: tk.Tk, file: str,
            title: str,  # description: str,
            price: str
            ) -> ttk.Frame:
    box = ttk.Frame(parent)

    title_label = ttk.Label(
        box, text=title + f"   ¢{price}", font=("Futura", 10, "bold")
    )
    title_label.pack()

    img = ImageTk.PhotoImage(
        Image.open(file).resize((100, 100), Image.LANCZOS), master=box
    )
    image_label = ttk.Label(box, image=img)
    image_label.image = img
    image_label.pack()

    # description_label = ttk.Label(box, text=description, font=("Futura", 15))
    # description_label.pack()

    return box


class TasksGUI:
    """
    Main window for Mac machines (not styled because Mac overrides it).
    """

    def __init__(self, parent: tk.Tk) -> None:
        self.parent = parent

        # background image adapts to how many tasks you've progressed or
        # completed recently, dashboard shows splash text congratulating the
        # user

        self.task_names_list: list[str] = []

        shop_btn = ttk.Button(parent, text="Shop", command=self.goto_shop)
        shop_btn.grid(row=0, sticky="w", padx=5)

        row1_lbl = ttk.Label(parent, text="Row1")
        row1_lbl.grid(row=1)

        for user in user_list:
            if user.active:
                recent_tasks: list[Task] = []
                for task in task_list:
                    print(task)

        gui_tasks: list[ttk.Frame] = []
        task_grid = ttk.Frame(parent)

        listlength = len(task_list)  # = 11
        columns: int = 5
        rows = int(listlength / columns)  # = 2.2 rnd to 2
        last_column = listlength % columns  # = 1
        for i in range(rows):
            for j in range(columns):
                index = i*columns+j
                gui_tasks.append(
                    create_task_element(
                        task_grid, task_list[index].image,
                        task_list[index].name,  # task_list[i].description
                    )
                )
                gui_tasks[index].grid(
                    row=i+2, column=j, padx=5, pady=5
                )
        for k in range(last_column):
            index = i*columns+j+k+1
            gui_tasks.append(
                create_task_element(
                    task_grid, task_list[index].image,
                    task_list[index].name,  # task_list[i].description
                )
            )
            gui_tasks[index].grid(
                row=rows+3, column=k, padx=5, pady=5
            )

        task_grid.grid(rowspan=5, columnspan=5)  # change to be responsive

        parent.bind("<Key>", self.event_handler)

    def event_handler(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            for user in user_list:
                user.active = False
            self.parent.destroy()

    def goto_shop(self) -> None:
        self.parent.destroy()
        new_windows("Shop")


class ShopGUI:

    def __init__(self, parent: tk.Tk) -> None:
        self.parent = parent

        back_btn = ttk.Button(parent, text="<-", command=self.goto_tasks)
        back_btn.grid(row=0, sticky="w", padx=5)

        example_items: list[Item] = []
        gui_ex_items: list[ttk.Frame] = []
        item_grid = ttk.Frame(parent)
        placeholder = ttk.Frame(item_grid, width=200, height=200)
        placeholder.grid_propagate(1)
        for i in range(4):
            for j in range(5):
                example_items.append(
                    Item("Example", "hellyeah.png", "An example item", 0)
                )
                example_items[i].test()
                gui_ex_items.append(
                    create_shop_item(
                        item_grid, example_items[i].image,
                        example_items[i].name, example_items[i].description,
                        example_items[i].price
                    )
                )
                gui_ex_items[5 * i + j].grid(
                    row=i + 1, column=j, padx=5, pady=5
                )
        item_grid.grid(rowspan=5, columnspan=5)  # change to be responsive

        parent.bind("<Key>", self.event_handler)

    def event_handler(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            for user in user_list:
                user.active = False
            self.parent.destroy()

    def goto_tasks(self) -> None:
        self.parent.destroy()
        new_windows("Tasks")


if __name__ == "__main__":
    user_list: list[User] = []
    with open("user_info.txt") as file:
        users = file.readlines()
        for user in users:
            user_list.append(User(user.split(",")))

    task_list: list[Task] = []
    with open("task_list.txt") as file:
        tasks = file.readlines()
        for task in tasks:
            task_list.append(Task(task.split(",")))

    # item_list: list[Item] = []
    # with open("item_list.txt") as file:
    #     items = file.readlines()
    #     for item in items:
    #         item_list.append(Item(item.split(",")))

    new_windows("Login")
    # new_windows("Tasks")
