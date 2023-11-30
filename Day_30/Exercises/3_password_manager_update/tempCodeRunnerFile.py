    if len(website) == 0:
            messagebox.showinfo(title="OOPs (EMPTY WEB FIELD)", message="Hey! Don't leave any of the fields empty.")
            website_entry.focus()
            break
        elif len(email) == 0:
            messagebox.showinfo(title="OOPs (EMPTY EMAIL FIELD)", message="Hey! Don't leave any of the fields empty.")
            email_entry.focus()
            break
        elif len(password) == 0 or len(password) < 5:
            messagebox.showinfo(title="OOPs (short/empty Password field!)", message="Password needs to be at least 5 characters or more.")
            pass_entry.delete(0, END)
            pass_entry.focus()
            break
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n{email}\n{password}\nIs it Ok to save?")
            if is_ok:
                try:
                    with open("data.json", "r") as file:
                        # Reading old data
                        data = json.load(file)

                except FileNotFoundError:
                    # If file does not exist, create an empty data dictionary
                    data = {}

                # Add the new data to the existing data dictionary
                new_data = {website: {"email": email, "password": password}}
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()
                break