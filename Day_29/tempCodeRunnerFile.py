    is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\n{email}\n{password}\nIs it Ok to save?")
            if is_ok:
                with open(file_name, mode="a") as file:
                    file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0,END)
                    email_entry.delete(0,END)
                    pass_entry.delete(0,END)
                break